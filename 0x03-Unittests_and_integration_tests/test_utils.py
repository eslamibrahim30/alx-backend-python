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
            ("One nested map", {"a": {"b": 2}}, ("a",), {"b": 2}),
            ("Double nested map", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, _, nested_map, path, expected):
        """
        This method for testing utils.access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
