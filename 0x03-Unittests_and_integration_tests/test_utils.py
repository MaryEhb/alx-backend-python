#!/usr/bin/env python3
'''unit tests for Utils.py'''
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    '''unit test for utils.access_nested_map'''

    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2]
    ])
    def test_access_nested_map(self, input_list, path, return_val):
        '''test that the method returns what it is supposed to.'''
        self.assertEqual(access_nested_map(input_list, path), return_val)

    @parameterized.expand([
        [{}, ("a",), 'a'],
        [{"a": 1}, ("a", "b"), 'b']
    ])
    def test_access_nested_map_exception(self, input_list, path, key):
        '''test that a KeyError is raised'''
        with self.assertRaises(KeyError) as raises:
            access_nested_map(input_list, path)
        self.assertEqual(raises.exception.args[0], key)


class TestGetJson(unittest.TestCase):
    '''unit test for utils.get_json'''

    @parameterized.expand([
        ["http://example.com", {"payload": True}],
        ["http://holberton.io", {"payload": False}]
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        '''test that utils.get_json returns the expected result'''
        mock_res = Mock()
        mock_res.json.return_value = test_payload
        mock_get.return_value = mock_res

        val = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(val, test_payload)


class TestMemoize(unittest.TestCase):
    '''unit test for utils.memoize'''

    def test_memoize(self):
        '''testing memorize method'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_f:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_f.assert_called_once()


if __name__ == '__main__':
    unittest.main()
