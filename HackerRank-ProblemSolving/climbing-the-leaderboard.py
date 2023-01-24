#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

# time exceeding
# def getRank(ranked,el):
#     rank = 1
#     for i in range(len(ranked)):
#         if ranked[i] < ranked[i-1]:
#             rank += 1
#         if ranked[i] == el:
#             return rank

# def getRank(ranked,el):
#     rank = 1
#     i = 0
#     n = True
#     while n:
#         if ranked[i] < ranked[i-1]:
#             rank += 1
#         if ranked[i] == el:
#             n = False
#             break
#         i += 1
#     return rank

# def climbingLeaderboard(ranked, player):
#     res = []
#     for i in player:
#         ranked.append(i)
#         ranked.sort(reverse=True)
#         # print(ranked)
#         res.append(getRank(ranked,i))
#     return res

def climbingLeaderboard(ranked, player):
    res = []
    ranked.sort()
    for j in range(len(player)):
        element = player[j]
        u = ranked.copy()
        for i in range(len(ranked)):
            if i == 0:
                if element <= ranked[i]:
                    u = [element] + ranked
                    res.append((sorted(list(set(u[::-1])),reverse=True).index(element))+1)
                    break
                elif element in range(ranked[i-1],ranked[i]):
                    u = [ranked[i]] + [element] + ranked[i+1:]
                    res.append((sorted(list(set(u[::-1])),reverse=True).index(element))+1)
                    break
            elif i == len(ranked) - 1:
                if element in range(ranked[i-1],ranked[i]):
                    u = ranked[:i] + [element] + [ranked[i]]
                    res.append((sorted(list(set(u[::-1])),reverse=True).index(element))+1)
                    break
                elif element >= ranked[i]:
                    u = ranked + [element]
                    res.append((sorted(list(set(u[::-1])),reverse=True).index(element))+1)
                    break
            else:
                if element in range(ranked[i-1]-1,ranked[i]+1):
                    u = ranked[:i] + [element] + ranked[i:]
                    res.append((sorted(list(set(u[::-1])),reverse=True).index(element))+1)
                    break
        ranked = u
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
