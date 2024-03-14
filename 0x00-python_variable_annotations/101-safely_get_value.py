#!/usr/bin/env python3
"""
This module for task "Duck typing - first element of a sequence"
"""
from typing import Mapping, Union, Any, TypeVar


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[TypeVar("T"), None] = None
        ) -> Union[Any, TypeVar("T")]:
    """
    This function returns a value for a given key in a given dct
    """
    if key in dct:
        return dct[key]
    else:
        return default
