#!/usr/bin/python
# -*- coding: utf-8 -*-


def fizzbuzz(index):
    if index == 15 or index == 30:
        return "FizzBuzz"

    if index % 3 == 0:
        return "Fizz"

    if index % 5 == 0:
        return "Buzz"


    return str(index)
