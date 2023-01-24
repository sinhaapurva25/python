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
    # Write your code here
    p = [0]
    k = 0
    for i in path:
        if i == 'U':
            k += 1
        else:
            k -= 1
        p.append(k)
    print(p)
    qq = list()    
    for i in range(len(p)):
        if p[i] == 0:
            qq.append(i)
    print(qq)
    q = [[qq[i],qq[i+1]] for i in range(len(qq)-1)]
    print(q)
    res = 0
    for i in q:
        print(p[i[0]+1:i[1]])
        if len(p[i[0]+1:i[1]]) == sum([1 for j in p[i[0]+1:i[1]] if j < 0]):
            res += 1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()


# steps = 8
# path = 'UDDDUDUU'
# result = countingValleys(steps, path)
# print(result)