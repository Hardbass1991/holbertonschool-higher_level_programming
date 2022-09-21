#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import sys
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, -4, 69]), 69)

    def test_types(self):
        self.assertRaises(TypeError, max_integer, ["s", 1, 4, 34])
        self.assertRaises(TypeError, max_integer, 1434.433)
        self.assertRaises(TypeError, max_integer, None)
