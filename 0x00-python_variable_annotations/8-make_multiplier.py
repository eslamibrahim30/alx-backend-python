#!/usr/bin/env python3
"""
This module for task "Complex types - functions"
"""
from typing import Callable
from typing import Union


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier
    """
    def multiply(num: float) -> float:
        """
        This function task a float number and multiply it by a multiplier
        """
        return num * multiplier
    return multiply
