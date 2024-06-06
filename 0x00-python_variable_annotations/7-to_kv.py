#!/usr/bin/env python3
'''7. Complex types - string and int/float to tuple'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''hat takes a string k and an int OR float v and
    returns a tuple of them'''
    return (k, v ** 2)
