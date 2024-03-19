#!/usr/bin/env python3
"""
This module for task
"Let's execute multiple coroutines at the same time with async"
"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """
    This async routine returns the list of all the delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    results.sort()
    return results
