#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    lr_diagonal = 0
    rl_diagonal = 0
    p = 0
    for i in arr:
        lr_diagonal += i[p]
        p += 1
    p = -1
    for i in arr:
        rl_diagonal += i[p]
        p -= 1
    return max(lr_diagonal,rl_diagonal)-min(lr_diagonal,rl_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
