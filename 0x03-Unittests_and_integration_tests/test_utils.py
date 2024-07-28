#!/usr/bin/env python3
'''0. Parameterize a unit test'''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''the first unit test for utils.access_nested_map'''

    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2]
    ])
    def test_access_nested_map(self, input_list, path, return_val):
        '''test that the method returns what it is supposed to.'''
        self.assertEqual(access_nested_map(input_list, path), return_val)
