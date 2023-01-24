#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    highest_scores = []
    lowest_scores = []
    for i in range(len(scores)):
        highest_scores.append(max(scores[:i+1]))
        lowest_scores.append(min(scores[:i+1]))
    return [len(list(set(highest_scores))[1:]),len(list(set(lowest_scores))[1:])]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
