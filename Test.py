#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from Cli import fizzbuzz


class SimpleTestCase(unittest.TestCase):

    testCases = [
        [1, "1"],
        [2, "2"],
        [3, "Fizz"],
        [4, "4"],
        [5, "Buzz"],
        [6, "Fizz"],
        [7, "7"],
        [8, "8"],
        [9, "Fizz"],
        [10, "Buzz"],
    ]

    def test_TestCases(self):
        for testCase in self.testCases:
            result = fizzbuzz(testCase[0])
            self.assertEqual(testCase[1], result)


if "__main__" == __name__:
    unittest.main()

