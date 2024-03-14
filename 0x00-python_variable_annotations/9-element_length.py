#!/usr/bin/env python3
"""
This module for task "Let's duck type an iterable object"
"""
from typing import Iterable, Sequence, Union, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function returns the length of each element in a given array
    """
    return [(i, len(i)) for i in lst]
