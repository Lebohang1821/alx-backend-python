#!/usr/bin/env python3
'''Asyncio Tasks'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''It asynchronously waits for random durations n times'''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n))))
    return sorted(wait_times)
