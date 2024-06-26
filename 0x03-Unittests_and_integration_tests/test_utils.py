#!/usr/bin/env python3
"""
This module for project "Unittests and Integration Tests"
"""
import unittest
import requests
import json
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from utils import memoize
from unittest.mock import patch
from unittest.mock import Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    This class for testing utils.access_nested_map function.
    """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {'b': 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        This method tests the access_nested_map normal execution.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        This method tests the access_nested_map exception.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    This class for testing the utils.get_json method.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        This method tests teh get_json normal execution without
        any dependency.
        """
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    This class for testing the utils.memoize method.
    """
    def test_memoize(self):
        """
        This method tests the normal execution of memoize method.
        """
        class TestClass:
            """
            This class is used to create a sample object for testing.
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        mem = TestClass()
        with patch.object(TestClass, 'a_method') as mock_a:
            mock_a.return_value = 42
            self.assertEqual(mem.a_property, 42)
            self.assertEqual(mem.a_property, 42)
            mock_a.assert_called_once()


if __name__ == '__main__':
    unittest.main()
