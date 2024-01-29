#!/usr/bin/python3
from functools import reduce
import operator


def factorize(natural_num):
    """
    factorize: Factorizes a number into a
    product of two smaller numbers
    Parameters:
    - natural_num: The number to be factorized

    Return:
    The two factors of the natural number and the natural number
    """
    first_factr = 2
    while (natural_num % first_factr):
        if (first_factr <= natural_num):
            first_factr += 1

    second_factr = natural_num // first_factr
    return [second_factr, first_factr, natural_num]
