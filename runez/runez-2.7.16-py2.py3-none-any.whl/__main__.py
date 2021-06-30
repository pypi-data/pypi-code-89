"""
See some example behaviors of runez
"""

import argparse
import logging
import os
import sys
import time

import runez
from runez.ascii import AsciiAnimation
from runez.inspector import ImportTime, run_cmds
from runez.render import NAMED_BORDERS, PrettyTable


def cmd_colors():
    """Show a coloring sample"""
    parser = argparse.ArgumentParser(description="Show a coloring sample")
    parser.add_argument("--border", choices=NAMED_BORDERS, help="Use custom border.")
    parser.add_argument("--color", action="store_true", help="Use colors (on by default on ttys).")
    parser.add_argument("--no-color", action="store_true", help="Do not use colors (even if on tty).")
    parser.add_argument("--bg", help="Show bg variant(s) (comma-separated list of color names).")
    parser.add_argument("--flavor", help="Show specific flavor (neutral, light or dark).")
    args = parser.parse_args()

    enable_colors = None
    if args.no_color:
        enable_colors = False

    elif args.color:
        enable_colors = True

    with runez.ActivateColors(enable=enable_colors, flavor=args.flavor):
        print("Backend: %s" % runez.color.backend)
        _show_fgcolors(border=args.border)
        if args.bg:
            for name in runez.flattened(args.bg, split=","):
                color = runez.color.bg.get(name)
                if color is None:
                    print("Unknown bg color '%s'" % name)

                else:
                    _show_fgcolors(bg=color, border=args.border)


def cmd_diagnostics():
    """Show system diagnostics sample"""
    parser = argparse.ArgumentParser(description="Show system diagnostics sample")
    parser.add_argument("--border", default="colon", choices=NAMED_BORDERS, help="Use custom border.")
    args = parser.parse_args()

    print(PrettyTable.two_column_diagnostics(runez.SYS_INFO.diagnostics(), border=args.border))


def cmd_import_speed():
    """Show average import time of top-level python packages installed in this venv"""
    parser = argparse.ArgumentParser(description="Show average import time of top-level python packages installed in this venv")
    parser.add_argument("--all", action="store_true", help="Show all.")
    parser.add_argument("--border", choices=NAMED_BORDERS, default="reddit", help="Use custom border.")
    parser.add_argument("--iterations", "-i", type=int, default=3, help="Number of measurements to average.")
    parser.add_argument("name", nargs="*", help="Names of modules to show (by default: all).")
    args = parser.parse_args()
    names = []
    if args.name:
        names.extend(runez.flattened(args.name, split=","))

    if args.all:
        names.extend(_all_deps())

    if not names:
        sys.exit("Please specify module names, or use --all")

    names = sorted(runez.flattened(names, unique=True))
    times = []
    fastest = None
    slowest = None
    for name in names:
        t = ImportTime(name, iterations=args.iterations)
        times.append(t)
        if t.cumulative is None:
            continue

        if fastest is None or (t.cumulative < fastest.cumulative):
            fastest = t

        if slowest is None or t.cumulative > slowest.cumulative:
            slowest = t

    table = PrettyTable("Module,-X cumulative,Elapsed,Vs fastest,Note", border=args.border)
    table.header[3].align = "center"
    mid = _get_mid(times) or 0
    for t in sorted(times):
        if t.cumulative is None:
            c = e = f = None

        else:
            factor = t.elapsed / fastest.elapsed
            c = runez.represented_duration(t.cumulative / 1000000, span=-2)
            e = runez.represented_duration(t.elapsed, span=-2)
            f = "x%.2f" % factor
            if t is fastest:
                f = ""

            elif t is slowest:
                f = runez.red(f)

            elif t.elapsed and t.elapsed > mid:
                f = runez.orange(f)

        table.add_row(t.module_name, c, e, f, t.problem or "")

    print(table)


def cmd_passthrough():
    """Run a program, capture its output as well as pass it through as-is (preserving terminal colors etc)"""
    parser = argparse.ArgumentParser(description="Capture pass-through test")
    # parser.add_argument("args", nargs="*", help="Command to run")
    args, unknown = parser.parse_known_args()

    unknown = runez.flattened(unknown, split=" ")
    if not unknown:
        sys.exit("Provide command to run")

    print("-- Running: %s\n" % unknown)
    r = runez.run(*unknown, fatal=False, passthrough=True)
    print("\n---- Captured: ----")
    print("\nstdout:\n%s" % (r.output or runez.dim("-empty-")))
    print("\nstderr:\n%s" % (r.error or runez.dim("-empty-")))


def cmd_progress_bar():
    """Show a progress bar sample"""
    names = AsciiAnimation.available_names()
    parser = argparse.ArgumentParser(description="Show a progress bar sample")
    parser.add_argument("--delay", "-d", type=float, default=100.0, help="Time in milliseconds to sleep between iterations.")
    parser.add_argument("--iterations", "-i", type=int, default=100, help="Number of iterations to run.")
    parser.add_argument("--log-every", "-l", type=int, default=5, help="Log a message every N iterations.")
    parser.add_argument("--spinner", "-s", choices=names, default=None, help="Pick spinner to use.")
    parser.add_argument("--sleep", type=float, default=None, help="Extra sleep when done, useful for inspecting animation a bit further.")
    parser.add_argument("--no-spinner", "-n", action="store_true", help="Useful to compare CPU usage with and without spinner.")
    parser.add_argument("--verbose", "-v", action="store_true", help="More chatty output.")
    parser.add_argument("name", nargs="*", help="Names of modules to show (by default: all).")
    args = parser.parse_args()

    process = None
    try:
        import psutil

        process = psutil.Process(os.getpid())
        process.cpu_percent()

    except ImportError:  # pragma: no cover
        pass

    runez.log.setup(console_format="%(levelname)s %(message)s", console_level=logging.INFO, trace="RUNEZ_DEBUG")
    if not args.no_spinner:
        runez.log.progress.start(frames=args.spinner, max_columns=40, spinner_color=runez.yellow)

    logger = logging.info if args.verbose else logging.debug
    for i in runez.ProgressBar(range(args.iterations)):
        i += 1
        if args.log_every and i % args.log_every == 0:
            logger("Running\niteration %s %s", runez.red(i), "-" * 50)
            logger = logging.debug

        else:
            runez.log.trace("At iteration %s" % i)

        if args.verbose and i % 10 == 0:  # pragma: no cover
            print("iteration %s" % runez.bold(i))

        if i == 42:  # pragma: no cover
            runez.log.progress.show("some progress msg")  # debug() and trace() messages don't appear any more after this
            for _ in runez.ProgressBar(range(10)):
                time.sleep(0.1)

        time.sleep(args.delay / 1000)

    msg = "done"
    if process:
        cpu_usage = ("%.2f" % process.cpu_percent()).rstrip("0")
        msg += " (%s%% CPU usage)" % cpu_usage

    print(msg)
    if args.sleep:
        runez.log.progress.show(msg)
        time.sleep(args.sleep)


def cmd_retry():
    """Exercise retry() decorator"""
    parser = argparse.ArgumentParser(description="Show a progress bar sample")
    parser.add_argument("--tries", "-t", type=int, default=runez.UNSET, help="Number of times to retry.")
    parser.add_argument("--delay", "-d", type=float, default=runez.UNSET, help="Initial delay in seconds between attempts.")
    parser.add_argument("--max-delay", "-m", type=float, default=runez.UNSET, help="Maximum delay in seconds.")
    parser.add_argument("--backoff", "-b", type=float, default=runez.UNSET, help="Initial delay in seconds between attempts.")
    parser.add_argument("--jitter", "-j", type=float, default=runez.UNSET, help="Random extra seconds to delay, between 0 and 'jitter'.")
    parser.add_argument("--fail", "-f", type=int, default=-1, help="How many times to fail (-1: infinite).")
    parser.add_argument("--iterations", "-i", type=int, default=0, help="Skip sleep(), show average retry times.")
    parser.add_argument("--timeout", type=int, default=0, help="Simulate function timeout (example: requests.get() timeout).")
    args = parser.parse_args()

    runez.log.setup(console_format="%(message)s", console_level=logging.INFO)
    args.iterations = runez.capped(args.iterations, minimum=0)
    args.timeout = runez.capped(args.timeout, minimum=0)
    args.logger = logging.info

    def on_log(message):
        args.logger(message)

    rh = runez.system.RetryHandler(
        tries=args.tries, delay=args.delay, max_delay=args.max_delay, backoff=args.backoff, jitter=args.jitter, logger=on_log
    )

    @rh.decorator
    def func(args):
        args.retry_count += 1
        args.remaining_fails -= 1
        if args.remaining_fails:
            msg = runez.red(u"oops - failed")
            if args.retry_count > 1:
                if args.cumulative_sleep:
                    elapsed = args.cumulative_sleep

                else:
                    elapsed = time.time() - args.started

                elapsed = runez.represented_duration(elapsed, span=-2)
                msg = u"+%s %s" % (runez.orange(elapsed), msg)

            args.cumulative_sleep += args.timeout
            raise Exception(msg)

        return runez.green(u"returned successfully")

    if args.iterations:
        def cumnulate_sleep(n):
            args.cumulative_sleep += n

        runez.system.sleep = cumnulate_sleep

    fail_note = " %s," % runez.orange(runez.plural(args.fail, "max failure")) if args.fail >= 0 else ""
    if args.timeout:
        fail_note += u" timeout %s," % runez.blue(runez.represented_duration(args.timeout, span=2))

    print(u"Running with%s %s\n" % (fail_note, runez.bold(rh)))
    result = None
    args.cumulative_sleep = 0.0
    total_time = 0.0
    args.started = time.time()
    for i in range(max(1, args.iterations)):
        try:
            total_time += args.cumulative_sleep
            args.cumulative_sleep = 0.0
            args.remaining_fails = args.fail + 1
            args.retry_count = 0
            result = func(args)

        except Exception as e:
            result = e

        args.logger = runez.log.trace

    retry_count = runez.plural(args.retry_count, "retry")
    if args.iterations:
        elapsed = u"%s on average" % runez.represented_duration(total_time / args.iterations, span=2)
        retry_count = u"%s of %s" % (runez.plural(args.iterations, "iteration"), retry_count)

    else:
        elapsed = runez.represented_duration(time.time() - args.started, span=-2)

    print(u"%s\n\nDone in %s, %s" % (result, runez.bold(elapsed), runez.bold(retry_count)))


def _get_mid(times):
    times = [t for t in times if t.elapsed]
    if times:
        times = sorted(times, key=lambda x: -x.elapsed)  # Don't fail if no elapsed available
        return times[int(len(times) / 2)].elapsed


def main():
    run_cmds()


def _show_fgcolors(bg=runez.plain, border=None):
    print("")
    table = PrettyTable("Color,Blink,Bold,Dim,Invert,Italic,Strikethrough,Underline", border=border)
    table.header.style = "bold"
    for color in runez.color.fg:
        color_name = color.name
        text = color(color.name)
        if text[0] == "\033":
            i = text.index("m", 1)
            text = "%s %s" % (color_name, text[2:i])

        line = [bg(color(text))]
        for style in runez.color.style:
            # text = "%s %s" % (style.name, color_name)
            line.append(bg(style(color(color_name))))

        table.add_row(line)

    print(table)


def _all_deps():
    """All dependencies in current venv"""
    import pkg_resources
    import sysconfig

    result = []
    base = sysconfig.get_path("purelib")
    ws = pkg_resources.WorkingSet([base])
    for dist in ws:
        if _is_interesting_dist(dist.key):
            top_level = _find_top_level(base, dist)
            if top_level:
                result.append(top_level)

    return result


# Usual dev libs that are not interesting for --all import times, they import ultra fast...
# They can always be stated as argument explicitly to show their import times anyway
DEV_LIBS = """
attrs coverage more-itertools packaging pip pluggy py pyparsing python-dateutil setuptools six wcwidth wheel zipp
binaryornot cookiecutter click future
"""
DEV_LIBS = set(runez.flattened(DEV_LIBS.splitlines(), split=" "))


def _is_interesting_dist(key):
    if key.startswith("pytest") or key.startswith("importlib"):
        return False

    return key not in DEV_LIBS


def _find_top_level(base, dist):
    name = dist.key.replace("-", "_").replace(".", "_")
    top_level = os.path.join(base, "%s-%s.dist-info" % (name, dist.version), "top_level.txt")
    for line in runez.readlines(top_level, default=[]):
        if not line.startswith("_") and line:
            return line


if __name__ == "__main__":
    main()
