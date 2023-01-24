#!/bin/python3

import math
from operator import rshift
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # if len(s) == 1:
    #     if s == 'a':
    #         return n
    #     else:
    #         return 0
    # else:
    #     # if n%len(s) == 0:
    #     #     s *= n//len(s)
    #     # else:
    #     #     s *= (n//len(s))+1
    #     # return sum([1 for i in s if i=='a'])
    return sum([1 for i in s if i == 'a']) * (n//len(s)) + sum([1 for i in s[:n%len(s)] if i == 'a'])
print(repeatedString('abcac',10))
print(repeatedString('aba',10))
print(repeatedString('a',1000000000000))
print(repeatedString('aab',882787))
print(repeatedString('x',970770))
print(repeatedString('ababa',3))