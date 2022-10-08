#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest
import io
import sys
import json

class TestInputValues(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(1, 2)
        self.rect2 = Rectangle(1, 2, 3)
        self.rect3 = Rectangle(1, 2, 3, 4)
        self.rect4 = Rectangle(1, 2, 3, 4, 5)
        self.rect5 = Rectangle(2, 4, 6, 9, 69)
        self.rect6 = Rectangle(3, 4)

    def tearDown(self):
        items = [self.rect1, self.rect2, self.rect3, self.rect4]
        items.extend([self.rect5, self.rect6])
        for item in items:
            del item
        Rectangle.__nb_objects = 0

    def test_attributes_were_stored_properly(self):
        self.assertEqual(self.rect1.width, 1)
        self.assertEqual(self.rect1.height, 2)
        self.assertEqual(self.rect2.x, 3)
        self.assertEqual(self.rect3.y, 4)
        self.assertEqual(self.rect4.id, 5)
    
    def test_wrong_type_inputs(self):
        lsts  = [["1", 2], [1, "2"], [1, 2, "3"], [1, 2, 3, "4"]]
        attrs = ["width", "height", "x", "y"]
        for i in range(len(lsts)):
            try:
                a = Rectangle(*lsts[i])
            except Exception as e:
                self.assertEqual(e.args[0], attrs[i] + " must be an integer")

    def test_wrong_value_inputs(self):
        lsts = [[-1, 2], [1, -2], [1, 2, -3], [1, 2, 3, -4], [0, 2], [1, 0]]
        attrs = ["width", "height", "x", "y", "width", "height"]
        for i in range(len(lsts)):
            ending = " must be > 0"
            if attrs[i] == "x" or attrs[i] == "y":
                ending = " must be >= 0"
            try:
                a = Rectangle(*lsts[i])
            except Exception as e:
                self.assertEqual(e.args[0], attrs[i] + ending)

    def test_area_str_and_display_methods(self):
        self.assertEqual(self.rect5.area(), 8)

        a = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(self.rect4.__str__(), a)

        a = '###\n###\n###\n###\n'
        printed_text = io.StringIO()
        sys.stdout = printed_text
        self.rect6.display()
        self.assertMultiLineEqual(printed_text.getvalue(), a)

        sys.stdout = sys.__stdout__

    def test_to_dictionary_method(self):
        a = self.rect5.to_dictionary()
        self.assertEqual(type(a), dict)
        str_rep = '{"height": 4, "id": 69, "width": 2, "x": 6, "y": 9}'
        sorted_a = dict(sorted(a.items()))
        self.assertEqual(str_rep, json.dumps(sorted_a))

    def test_update_method_args(self):
        r = self.rect5
        a = dict(sorted(r.to_dictionary().items()))
        r.update()
        b = dict(sorted(r.to_dictionary().items()))
        self.assertEqual(json.dumps(a), json.dumps(b))
        
        lsts = [[42], [42, 1], [42, 1, 2], [42, 1, 2, 3], [42, 1, 2, 3, 4]]

        for i in range(len(lsts)):
            r.update(*lsts[i])
            attrs = [r.id, r.width, r.height, r.x, r.y]
            for j in range(len(lsts[i])):
                self.assertEqual(lsts[i][j], attrs[j])

    def test_update_method_kwargs(self):
        r = self.rect5
        ks = ['id', 'width', 'height', 'x', 'y']
        vs = [89, 1, 2, 3, 4]
        d = {}

        for i in range(len(ks)):
            d[ks[i]] = vs[i]
            r.update(**d)
            to_dict = r.to_dictionary()
            for j in list(d.keys()):
                self.assertEqual(to_dict[j], d[j])

    def test_create_cls_method(self):
        ks = ['id', 'width', 'height', 'x', 'y']
        vs = [69, 5, 2, 3, 4]
        d = {}

        for i in range(len(ks)):
            d[ks[i]] = vs[i]
            r = Rectangle.create(**d)
            to_dict = r.to_dictionary()
            for j in list(d.keys()):
                self.assertEqual(to_dict[j], d[j])

    def test_save_to_file(self):
        inputs = [None, [], [Rectangle(1, 2)]]
        outputs = ['[]', '[]'] 
        a = '[{"id": 45, "width": 1, "height": 2, "x": 0, "y": 0}]'
        outputs.append(a)

        for i in range(len(inputs)):
            Rectangle.save_to_file(inputs[i])
            with open("Rectangle.json", "r", encoding="utf-8") as f:
                self.assertEqual(outputs[i], f.read())

    def test_load_from_file(self):
        dct = {"id": 45, "width": 1, "height": 2, "x": 0, "y": 0}
        saved_dct = Rectangle.load_from_file()[0].to_dictionary()
        for k, v in dct.items():
            self.assertEqual(saved_dct[k], v)
