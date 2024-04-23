#!/usr/bin/env python3
'''Task 0 async comprehension'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    The coroutine collects 10 random numbers
    using an async comprehensing
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
