#!/usr/bin/env python3
"""
This module for task "The basics of async"
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    This asynchronous coroutine waits for a random delay
    between 0 and max_delay.
    """
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time
