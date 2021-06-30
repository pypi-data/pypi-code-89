"""Generic utilities."""
from typing import (
    Any, Dict, Hashable, Iterable, List, Optional, Sequence, TypeVar,
)

import click

from cloup.typing import MISSING, Possibly

click_version_tuple = click.__version__.split('.')

T = TypeVar('T')
K = TypeVar('K', bound=Hashable)
V = TypeVar('V')


def pick_non_missing(d: Dict[K, Possibly[V]]) -> Dict[K, V]:
    return {key: val for key, val in d.items() if val is not MISSING}


def class_name(obj):
    return obj.__class__.__name__


def check_arg(condition: bool, msg: str = ''):
    if not condition:
        raise ValueError(msg)


def indent_lines(lines: Iterable[str], width=2) -> List[str]:
    spaces = ' ' * width
    return [spaces + line for line in lines]


def make_repr(obj, *args, _line_len: int = 60, _indent: int = 2, **kwargs) -> str:
    """
    Generate repr(obj).

    :param obj:
        object to represent
    :param args:
        positional arguments in the repr
    :param _line_len:
        if the repr length exceeds this, arguments will be on their own line;
        if negative, the repr will be in a single line regardless of its length
    :param _indent:
        indentation width of arguments in case they are shown in their own line
    :param kwargs:
        keyword arguments in the repr
    :return: str
    """
    cls_name = obj.__class__.__name__
    arglist = [
        *(repr(arg) for arg in args),
        *(f'{key}={value!r}' for key, value in kwargs.items()),
    ]
    len_arglist = sum(len(s) for s in arglist)
    total_len = len(cls_name) + len_arglist + 2 * len(arglist)
    if 0 <= _line_len < total_len:
        lines = indent_lines(arglist, width=_indent)
        args_text = ',\n'.join(lines)
        return f'{cls_name}(\n{args_text}\n)'
    else:
        args_text = ', '.join(arglist)
        return f'{cls_name}({args_text})'


def make_one_line_repr(obj, *args, **kwargs):
    return make_repr(obj, *args, _line_len=-1, **kwargs)


def pluralize(
    count: int, zero: str = '', one: str = '', many: str = '',
) -> str:
    if count == 0 and zero:
        return zero
    if count == 1 and one:
        return one
    return many.format(count=count)


def first_not_none(*values: Optional[T]) -> Optional[T]:
    """Returns the first value that is not None
    (or ``default`` if no such value exists)."""
    return next((val for val in values if val is not None), None)


def first_bool(*values: Optional[bool]) -> bool:
    """Returns the first bool (or raises StopIteration if no bool is found)."""
    return next(val for val in values if isinstance(val, bool))


def pick_not_none(iterable: Iterable[Optional[T]]) -> List[T]:
    return [x for x in iterable if x is not None]


def check_positive_int(value, arg_name):
    error_type = None
    if not isinstance(value, int):
        error_type = TypeError
    elif value <= 0:
        error_type = ValueError
    if error_type:
        raise error_type(f'{arg_name} should be a positive integer. It is: {value}.')


def identity(x: T) -> T:
    return x


class FrozenSpaceMeta(type):
    def __init__(cls, *args):
        d = {k: v for k, v in vars(cls).items() if not k.startswith('_')}
        type.__setattr__(cls, '_dict', d)

    def __setattr__(cls, key, value):
        raise Exception("you can't set attributes on this class")

    def asdict(cls) -> Dict[str, Any]:
        return cls._dict  # type: ignore

    def __contains__(cls, item: str) -> bool:
        return item in cls.asdict()

    def __getitem__(cls, item):
        return cls._dict[item]


class FrozenSpace(metaclass=FrozenSpaceMeta):
    """A class used just as frozen namespace for constants."""

    def __init__(self):
        raise Exception(
            "this class is just a namespace for constants, it's not instantiable.")


def delete_keys(d: dict, keys: Sequence[str]) -> None:
    for key in keys:
        del d[key]
