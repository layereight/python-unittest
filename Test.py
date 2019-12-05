#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from Cli import fizzbuzz


class SimpleTestCase(unittest.TestCase):

    def test_this(self):
        result = fizzbuzz(1)
        self.assertEqual("1", result)


if "__main__" == __name__:
    unittest.main()

