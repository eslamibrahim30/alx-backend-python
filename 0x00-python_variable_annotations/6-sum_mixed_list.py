#!/usr/bin/env python3
"""
This module for task "Complex types - mixed list"
"""
from typing import List
from typing import Union


def sum_mixed_list(input_list: List[Union[float, int]]) -> float:
    """
    This function takes a list mxd_lst of integers and floats
    and returns their sum as a float
    """
    return sum(input_list)
