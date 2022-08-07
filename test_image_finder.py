import time
import unittest
from unittest import TestCase

import image_finder


class MyTestCase(TestCase):
    finder = image_finder.img_finder()

    def test_nominal(self):
        bytes_array = self.finder.find(102)
        self.assertEqual(type(bytes_array), bytes)
        self.assertGreater(bytes_array.__sizeof__(), 0)

        bytes_array = self.finder.find(200)
        self.assertEqual(type(bytes_array), bytes)
        self.assertGreater(bytes_array.__sizeof__(), 0)

        bytes_array = self.finder.find(404)
        self.assertEqual(type(bytes_array), bytes)
        self.assertGreater(bytes_array.__sizeof__(), 0)

    def test_false(self):
        bytes_array = self.finder.find(2000002)
        self.assertEqual(bytes_array, None)
        bytes_array = self.finder.find(210)
        self.assertEqual(bytes_array, None)

    def test_Type_error(self):
        try:
            self.finder.find("this is wrong")
        except Exception as exception:
            self.assertEqual(TypeError, type(exception))

        try:
            self.finder.find("200")
        except Exception as exception:
            self.assertEqual(TypeError, type(exception))

    def test_optimization(self):
        start1 = time.time()
        bytes_array = self.finder.find(400)
        self.assertGreater(bytes_array.__sizeof__(), 0)
        end1 = time.time()
        # self.assertEqual(type(bytes_array), bytes)

        start2 = time.time()
        bytes_array = self.finder.find(400)
        self.assertGreater(bytes_array.__sizeof__(), 0)
        end2 = time.time()
        # self.assertEqual(type(bytes_array), bytes)

        self.assertGreater(end1 - start1, end2 - start2)

        start1 = time.time()
        bytes_array = self.finder.find(4000000004)
        end1 = time.time()
        # self.assertEqual(type(bytes_array), bytes)

        start2 = time.time()
        bytes_array = self.finder.find(4000000004)
        end2 = time.time()
        # self.assertEqual(type(bytes_array), bytes)

        self.assertGreater(end1 - start1, end2 - start2)


if __name__ == '__main__':
    unittest.main()
