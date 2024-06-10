#!/usr/bin/env python3
'''4. Tasks'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''takes in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay'''
    res = [await single
           for single in
           asyncio.as_completed([task_wait_random(max_delay)
                                 for _ in range(n)])]
    return res
