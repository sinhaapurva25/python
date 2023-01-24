#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    res = s[:8]
    hrs = int(s.split(":")[0])
    if s[::-1][:2] == 'MP':   
        if hrs < 12:
            res =  str(hrs+12)+s[2:8]
    else:
        if hrs == 12:
            res =  '00'+s[2:8]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
