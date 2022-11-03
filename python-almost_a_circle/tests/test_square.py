#!/usr/bin/python3
from models.square import Square
import unittest
import io
import sys
import json

class TestInputValues(unittest.TestCase):

    def setUp(self):
        self.sq1 = Square(1)
        self.sq2 = Square(1, 2)
        self.sq3 = Square(1, 2, 3, 90)
        self.sq4 = Square(1, 2, 3, 4)
        self.sq5 = Square(5, 0, 0, 69)

    def test_attributes_were_stored_properly(self):
        self.assertEqual(self.sq1.size, 1)
        self.assertEqual(self.sq1.height, 1)
        self.assertEqual(self.sq2.x, 2)
        self.assertEqual(self.sq3.y, 3)
        self.assertEqual(self.sq3.id, 90)
    
    def test_wrong_type_inputs(self):
        lsts  = [["1"], [1, "2"], [1, 2, "3"]]
        attrs = ["width", "x", "y"]
        for i in range(len(lsts)):
            try:
                a = Square(*lsts[i])
            except Exception as e:
                self.assertEqual(e.args[0], attrs[i] + " must be an integer")

    def test_wrong_value_inputs(self):
        lsts = [[-1], [1, -2], [1, 2, -3], [0]]
        attrs = ["width", "x", "y", "width"]
        for i in range(len(lsts)):
            ending = " must be > 0"
            if attrs[i] == "x" or attrs[i] == "y":
                ending = " must be >= 0"
            try:
                a = Square(*lsts[i])
            except Exception as e:
                self.assertEqual(e.args[0], attrs[i] + ending)

    def test_area_str_and_display_methods(self):
        self.assertEqual(self.sq5.area(), 25)

        a = "[Square] (69) 0/0 - 5"
        self.assertEqual(self.sq5.__str__(), a)

        a = '#####\n#####\n#####\n#####\n#####\n'
        printed_text = io.StringIO()
        sys.stdout = printed_text
        self.sq5.display()
        self.assertMultiLineEqual(printed_text.getvalue(), a)

        sys.stdout = sys.__stdout__

    def test_to_dictionary_method(self):
        a = self.sq5.to_dictionary()
        self.assertEqual(type(a), dict)
        str_rep = '{"id": 69, "size": 5, "x": 0, "y": 0}'
        sorted_a = dict(sorted(a.items()))
        self.assertEqual(str_rep, json.dumps(sorted_a))

    def test_update_method_args(self):
        r = self.sq5
        a = dict(sorted(r.to_dictionary().items()))
        r.update()
        b = dict(sorted(r.to_dictionary().items()))
        self.assertEqual(json.dumps(a), json.dumps(b))
        
        lsts = [[42], [42, 1], [42, 1, 2], [42, 1, 2, 3]]

        for i in range(len(lsts)):
            r.update(*lsts[i])
            attrs = [r.id, r.size, r.x, r.y]
            for j in range(len(lsts[i])):
                self.assertEqual(lsts[i][j], attrs[j])

    def test_update_method_kwargs(self):
        r = self.sq5
        ks = ['id', 'size', 'x', 'y']
        vs = [89, 6, 1, 1]
        d = {}

        for i in range(len(ks)):
            d[ks[i]] = vs[i]
            r.update(**d)
            to_dict = r.to_dictionary()
            for j in list(d.keys()):
                self.assertEqual(to_dict[j], d[j])

    def test_create_cls_method(self):
        ks = ['id', 'size', 'x', 'y']
        vs = [69, 5, 3, 4]
        d = {}

        for i in range(len(ks)):
            d[ks[i]] = vs[i]
            r = Square.create(**d)
            to_dict = r.to_dictionary()
            for j in list(d.keys()):
                self.assertEqual(to_dict[j], d[j])

    def test_save_to_file(self):
        inputs = [None, [], [Square(1, 0, 0, 999)]]
        outputs = ['[]', '[]'] 
        a = '[{"id": 999, "size": 1, "x": 0, "y": 0}]'
        outputs.append(a)

        for i in range(len(inputs)):
            Square.save_to_file(inputs[i])
            with open("Square.json", "r", encoding="utf-8") as f:
                self.assertEqual(outputs[i], f.read())

    def test_load_from_file(self):
        dct = {"id": 999, "size": 1, "x": 0, "y": 0}
        saved_dct = Square.load_from_file()[0].to_dictionary()
        for k, v in dct.items():
            self.assertEqual(saved_dct[k], v)
