#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import sys
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, -4, 69]), 69)
        self.assertAlmostEqual(max_integer([678, -4, 69]), 678)
        self.assertAlmostEqual(max_integer([1, 182, 69]), 182)
        self.assertAlmostEqual(max_integer([1, -4, 45]), 45)
        self.assertAlmostEqual(max_integer([-1, -4, -69]), -1)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1]), 1)

    def test_types(self):
        self.assertRaises(TypeError, max_integer, ["s", 1, 4, 34])
        self.assertRaises(TypeError, max_integer, 1434.433)
        self.assertRaises(TypeError, max_integer, None)
