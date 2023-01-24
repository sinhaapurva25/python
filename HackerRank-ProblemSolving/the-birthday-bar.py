#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#
import itertools
def birthday(s, d, m):
    if len(s)==1 and s[0]==d:
        return 1
    else:
        return sum([1 for i in range(len(s)-1) if (sum(s[i:i+m])==d)])
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

import os
op = [2, 0, 1, 3, 3, 2, 7, 6, 3, 3, 10, 13, 4, 16]
folder_path = r'C://Python-work//HackerRank//Problem Solving//the-birthday-bar-testcases//input_1'
for each_file in os.listdir(folder_path):
    f = open(os.path.join(folder_path, each_file),'r')
    line1 = f.readline()
    arr = [int(i) for i in f.readline().split()]
    d, m = map(int,f.readline().split())
    f.close()
    res = birthday(arr,d,m)
    print(each_file,res,op[int(str(each_file)[5:7])])