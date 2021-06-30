import sys
import time
import pytest

import ray
from ray.util import ActorPool


@pytest.fixture
def init():
    ray.init(num_cpus=4)
    yield
    ray.shutdown()


def test_get_next(init):
    @ray.remote
    class MyActor:
        def __init__(self):
            pass

        def f(self, x):
            return x + 1

        def double(self, x):
            return 2 * x

    actors = [MyActor.remote() for _ in range(4)]
    pool = ActorPool(actors)
    for i in range(5):
        pool.submit(lambda a, v: a.f.remote(v), i)
        assert pool.get_next() == i + 1


def test_get_next_unordered(init):
    @ray.remote
    class MyActor:
        def __init__(self):
            pass

        def f(self, x):
            return x + 1

        def double(self, x):
            return 2 * x

    actors = [MyActor.remote() for _ in range(4)]
    pool = ActorPool(actors)

    total = []

    for i in range(5):
        pool.submit(lambda a, v: a.f.remote(v), i)
    while pool.has_next():
        total += [pool.get_next_unordered()]

    assert all(elem in [1, 2, 3, 4, 5] for elem in total)


def test_map(init):
    @ray.remote
    class MyActor:
        def __init__(self):
            pass

        def f(self, x):
            return x + 1

        def double(self, x):
            return 2 * x

    actors = [MyActor.remote() for _ in range(4)]
    pool = ActorPool(actors)

    index = 0
    for v in pool.map(lambda a, v: a.double.remote(v), range(5)):
        assert v == 2 * index
        index += 1


def test_map_unordered(init):
    @ray.remote
    class MyActor:
        def __init__(self):
            pass

        def f(self, x):
            return x + 1

        def double(self, x):
            return 2 * x

    actors = [MyActor.remote() for _ in range(4)]
    pool = ActorPool(actors)

    total = []
    for v in pool.map(lambda a, v: a.double.remote(v), range(5)):
        total += [v]

    assert all(elem in [0, 2, 4, 6, 8] for elem in total)


def test_get_next_timeout(init):
    @ray.remote
    class MyActor:
        def __init__(self):
            pass

        def f(self, x):
            while True:
                x = x + 1
                time.sleep(1)
            return None

        def double(self, x):
            return 2 * x

    actors = [MyActor.remote() for _ in range(4)]
    pool = ActorPool(actors)
    pool.submit(lambda a, v: a.f.remote(v), 0)
    with pytest.raises(TimeoutError):
        pool.get_next_unordered(timeout=0.1)


def test_get_next_unordered_timeout(init):
    @ray.remote
    class MyActor:
        def __init__(self):
            pass

        def f(self, x):
            while True:
                x + 1
                time.sleep(1)
            return

        def double(self, x):
            return 2 * x

    actors = [MyActor.remote() for _ in range(4)]
    pool = ActorPool(actors)

    pool.submit(lambda a, v: a.f.remote(v), 0)
    with pytest.raises(TimeoutError):
        pool.get_next_unordered(timeout=0.1)


def test_multiple_returns(init):
    @ray.remote
    class Foo(object):
        @ray.method(num_returns=2)
        def bar(self):
            return 1, 2

    pool = ActorPool([Foo.remote() for _ in range(2)])
    for _ in range(4):
        pool.submit(lambda a, v: a.bar.remote(), None)

    while pool.has_next():
        assert pool.get_next(timeout=None) == [1, 2]


def test_pop_idle(init):
    @ray.remote
    class MyActor:
        def __init__(self):
            pass

        def f(self, x):
            return x + 1

        def double(self, x):
            return 2 * x

    actors = [MyActor.remote()]
    pool = ActorPool(actors)

    pool.submit(lambda a, v: a.double.remote(v), 1)
    assert pool.pop_idle() is None
    assert pool.has_free() is False  # actor is busy
    assert pool.get_next() == 2
    assert pool.has_free()
    pool.pop_idle()  # removes actor from pool
    assert pool.has_free() is False  # no more actors in pool


def test_push(init):
    @ray.remote
    class MyActor:
        def __init__(self):
            pass

        def f(self, x):
            return x + 1

        def double(self, x):
            return 2 * x

    a1, a2 = MyActor.remote(), MyActor.remote()
    pool = ActorPool([a1])

    pool.submit(lambda a, v: a.double.remote(v), 1)
    assert pool.has_free() is False  # actor is busy
    with pytest.raises(ValueError):
        pool.push(a1)
    pool.push(a2)
    assert pool.has_free()  # a2 is available


if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))
