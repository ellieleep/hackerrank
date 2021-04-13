#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    upcount = 0
    downcount = 0
    mountaincount = 0
    valleycount = 0
    pathlist = list(path)

    for i, step in enumerate(pathlist):
        if step == 'U':
            upcount += 1
        else:
            downcount += 1
        if (upcount - downcount >= 0) and (pathlist[i + 1] != 'D') and (pathlist[i - 1] != 'U'):
            mountaincount += 1
        elif (downcount - upcount <= 0) and (pathlist[i + 1] != 'U') and (pathlist[i - 1] != 'D'):
            valleycount += 1


steps = 8

path = 'UDDDUDUU'

result = countingValleys(steps, path)

print(result)
