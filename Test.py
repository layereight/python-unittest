#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from Cli import fizzbuzz


class SimpleTestCase(unittest.TestCase):

    def test_one(self):
        result = fizzbuzz(1)
        self.assertEqual("1", result)

    def test_two(self):
        result = fizzbuzz(2)
        self.assertEqual("2", result)

    def test_three(self):
        result = fizzbuzz(3)
        self.assertEqual("Fizz", result)

    def test_four(self):
        result = fizzbuzz(4)
        self.assertEqual("4", result)

    def test_five(self):
        result = fizzbuzz(5)
        self.assertEqual("Buzz", result)


if "__main__" == __name__:
    unittest.main()

