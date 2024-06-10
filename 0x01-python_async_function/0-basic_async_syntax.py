#!/usr/bin/env python3
'''0. The basics of async'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''takes in an integer that waits for a random delay between 0
    and that int and eventually returns it'''
    random_num = random.uniform(1, max_delay)
    await asyncio.sleep(random_num)
    return random_num
