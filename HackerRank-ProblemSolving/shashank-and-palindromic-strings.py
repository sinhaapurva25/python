#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'palindromicStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY a as parameter.
#

def palindromicStrings(a):
    # Write your code here
    palindromicSubsequences = []
    for wrd in a:
        for j in range(1, len(wrd)+1):
            subsequences = [''.join(k) for k in list(itertools.combinations(wrd,j))] 
            for k in subsequences:
                if k not in palindromicSubsequences and k == k[::-1]:
                    palindromicSubsequences.append(k)
    return len(palindromicSubsequences) % (10**9 + 7)

# a = [['aa','b','aa'],['a','b','c'],['abc','abc']]
# for arr in a:
#     result = palindromicStrings(arr)
#     print(str(result) + '\n')
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a_count = int(input().strip())

        a = []

        for _ in range(a_count):
            a_item = input()
            a.append(a_item)

        result = palindromicStrings(a)

        fptr.write(str(result) + '\n')

    fptr.close()
