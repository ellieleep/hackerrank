#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socksdict = {}
    for sock in ar:
        if sock in socksdict:
            socksdict[sock].append(sock)
        else:
            socksdict[sock] = [sock]

    matchedpairs = 0

    for sockslist in socksdict.values():
        matchedpairs += len(sockslist) // 2

    return matchedpairs

n = 9

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

result = sockMerchant(n, ar)
