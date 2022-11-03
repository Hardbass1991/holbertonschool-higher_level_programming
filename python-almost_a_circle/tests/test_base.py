#!/usr/bin/python3
import unittest
from models.base import Base

class TestID(unittest.TestCase):

    def setUp(self):
        self.base1 = Base()
        self.base2 = Base()
        self.base3 = Base(89)
    def test_auto_assign_id(self):
        self.assertEqual(type(self.base1.id), int)
    def test_augmenting_auto_id(self):
        self.assertEqual(self.base1.id, self.base2.id - 1)
    def test_passed_id_is_stored(self):
        self.assertEqual(self.base3.id, 89)

    def test_none_to_json_string(self):
        a = self.base1.to_json_string(None)
        self.assertEqual(a, "[]")
    def test_empty_to_json_string(self):
        a = self.base1.to_json_string([])
        self.assertEqual(a, "[]")
    def test_regular_to_json_string(self):
        a = self.base1.to_json_string( {'id': 69})
        self.assertIsNotNone(a)
        self.assertEqual(type(a), str)

    def test_none_from_json_string(self):
        a = self.base1.from_json_string(None)
        self.assertEqual(a, [])
    def test_empty_from_json_string(self):
        a = self.base1.from_json_string("[]")
        self.assertEqual(a, [])
    def test_regular_from_json_string(self):
        a = self.base1.from_json_string('[{ "id": 69}]')
        self.assertIsNotNone(a)
        self.assertEqual(type(a), list)
