#!/usr/bin/env python3
"""safely_get_value module"""

from re import T
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')  # Create a new type


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """Return the value in the dictionary specified by the key"""
    if key in dct:
        return dct[key]
    else:
        return default
