#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    # https://www.geeksforgeeks.org/lcm-of-given-array-elements/
    def gcd(x,y):   
        while(y):
            x, y = y, x % y
        return x
    LCM = a[0]
    for i in a:
        LCM = LCM * i / gcd(LCM,i)
    # https://www.geeksforgeeks.org/gcd-in-python/
    # https://www.geeksforgeeks.org/gcd-two-array-numbers/
    GCD = b[0]
    for i in b:
        GCD = gcd(GCD,i)
    return len([i for i in list(range(int(LCM),GCD+1,int(LCM))) if GCD%i==0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
