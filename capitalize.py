#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    name = [y.capitalize() for y in s.split(' ')]
    return ' '.join(name)


if __name__ == '__main__':
    fptr = open('file.txt', 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
