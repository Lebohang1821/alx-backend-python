#!/usr/bin/env python3
'''Task 3'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates asynchronous task for wait random'''
    return asyncio.create_task(wait_random(max_delay))
