#!/usr/bin/env python3
'''9. Let's duck type an iterable object'''
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''take list and return list of tuples of element and its len'''
    return [(i, len(i)) for i in lst]
