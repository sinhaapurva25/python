# a = 2
# apples = [5,6,7]
# s = 8
# t = 9
# for j in [a+i for i in apples]:
#     if j in list(range(8, 9+1)):
#         print(j)
# print([a+i for i in apples if a+i in list(range(s, t+1))])
# print(len([a+i for i in apples if a+i in list(range(s, t+1))]))
# find_in_range = list(range(s, t+1))
# print(len([a+i for i in apples if a+i in find_in_range]))
# APPLES = 0
# for i in apples:
#     if a+i in find_in_range:
#         APPLES += 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # find_in_range = list(range(s, t+1))
    # APPLES = 0
    # ORANGES = 0
    # for i in apples:
    #     if a+i >=s and a+i <=t:
    #         APPLES += 1
    # for i in oranges:
    #     if b+i >=s and b+i <=t:
    #         ORANGES += 1
    # print(APPLES)
    # print(ORANGES)
    
    # find_in_range = list(range(s, t+1))
    # print(len([a+i for i in apples if a+i in find_in_range]))
    # print(len([b+i for i in oranges if b+i in find_in_range]))
    
    print(len([a+i for i in apples if a+i >=s and a+i <=t]))
    print(len([b+i for i in oranges if b+i >=s and b+i <=t]))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
