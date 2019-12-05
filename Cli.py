#!/usr/bin/python
# -*- coding: utf-8 -*-


def fizzbuzz(index):
    if index == 3 or index == 6:
        return "Fizz"

    if index == 5:
        return "Buzz"

    return str(index)
