#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = sum(list(map(int, [i>0 for i in arr])))
    neg = sum(list(map(int, [i<0 for i in arr])))
    zer = sum(list(map(int, [i==0 for i in arr])))
    [print(i/len(arr)) for i in [pos, neg, zer]]

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
