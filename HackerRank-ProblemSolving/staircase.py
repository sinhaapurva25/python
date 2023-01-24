#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    arr =''
    k = n-1
    for i in range(n):
        row = ''
        for j in range(n):
            if j>=k:
                row += '#'
            else:
                row += ' '
        arr += row + '\n'
        k -= 1
    print(arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
