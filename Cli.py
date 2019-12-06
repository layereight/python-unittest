#!/usr/bin/python
# -*- coding: utf-8 -*-


def fizzbuzz(index):
    if index % 15 == 0:
        return "FizzBuzz"

    if index % 3 == 0:
        return "Fizz"

    if index % 5 == 0:
        return "Buzz"

    return str(index)


if "__main__" == __name__:
    for i in range(1, 101):
        print(fizzbuzz(i))
