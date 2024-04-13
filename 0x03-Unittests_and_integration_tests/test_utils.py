#!/usr/bin/env python3
"""
This module for project "Unittests and Integration Tests"
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    This class for testing utils.access_nested_map function.
    """
    @parameterized.expand([
            ("No nested map", {"a": 1}, ("a",), 1),
            ("One nested map", {"a": {"b": 2}}, ("a",), {'b': 2}),
            ("Double nested map", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, _, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
            ("Empty map", {}, ("a",)),
            ("Non-existent path", {"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, _, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
