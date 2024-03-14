#!/usr/bin/env python3
"""
This module for task "Duck typing - first element of a sequence"
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function returns the first element in a given array
    """
    if lst:
        return lst[0]
    else:
        return None
