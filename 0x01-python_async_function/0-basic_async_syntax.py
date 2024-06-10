#!/usr/bin/env python3
'''0. The basics of async'''

import asyncio
import random


async def wait_random(max_delay=10):
    '''takes in an integer that waits for a random delay between 0
    and that int and eventually returns it'''
    random_num = random.uniform(0, max_delay)
    asyncio.sleep(random_num)
    return random_num
