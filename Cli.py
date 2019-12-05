#!/usr/bin/python
# -*- coding: utf-8 -*-


def fizzbuzz(index):

    result_string = ""

    if index % 3 == 0:
        result_string = "Fizz"

    if index % 5 == 0:
        result_string += "Buzz"
        return result_string

    if result_string == "":
        result_string = str(index)

    return result_string
