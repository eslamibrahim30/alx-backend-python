#!/usr/bin/env python3
"""
This module for task "Async Comprehensions"
"""
import random
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    This asynchronous coroutine will collect 10 random numbers
    using an async comprehensing over async_generator,
    then return the 10 random numbers.
    """
    return [i async for i in async_generator()]