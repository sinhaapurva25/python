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

# def getRank(ranked,el):
#     return [sorted(list(set(ranked)),reverse=True).index(el)+1 for i in scores]

# def climbingLeaderboard(ranked, player):
#     res = []
#     for i in player:
#         ranked.append(i)
#         ranked.sort(reverse=True)
#         # print(ranked)
#         res.append(getRank(ranked,i))
#     return res

# def climbingLeaderboard(ranked, player):
#     res = []
#     ranked.sort()
#     for j in player:
        
#         u = ranked.copy()
#         lenRanked = len(ranked)
#         for i in range(lenRanked):
#             if i == 0:
#                 if j <= ranked[i]:
#                     u = [j] + ranked
#                     res.append((sorted(list(set(u[::-1])),reverse=True).index(j))+1)
#                     break
#                 elif j in range(ranked[i-1],ranked[i]):
#                     u = [ranked[i]] + [j] + ranked[i+1:]
#                     res.append((sorted(list(set(u[::-1])),reverse=True).index(j))+1)
#                     break
#             elif i == lenRanked - 1:
#                 if j in range(ranked[i-1],ranked[i]):
#                     u = ranked[:i] + [j] + [ranked[i]]
#                     res.append((sorted(list(set(u[::-1])),reverse=True).index(j))+1)
#                     break
#                 elif j >= ranked[i]:
#                     u = ranked + [j]
#                     res.append((sorted(list(set(u[::-1])),reverse=True).index(j))+1)
#                     break
#             else:
#                 if j in range(ranked[i-1]-1,ranked[i]+1):
#                     u = ranked[:i] + [j] + ranked[i:]
#                     res.append((sorted(list(set(u[::-1])),reverse=True).index(j))+1)
#                     break
#         ranked = u
#     return res

# from bisect import bisect_right

# def climbingLeaderboard(ranked, player):
#     rr = list(dict.fromkeys(ranked))[::-1]
#     lr = len(rr)
#     return [lr - bisect_right(rr, p) + 1 for p in player]

def climbingLeaderboard(scores, newPlayersScores):
    def getInitRank(scores):
        uniqueRanked = sorted(list(set(scores)),reverse=True)
        return [uniqueRanked.index(i)+1 for i in scores]

    rankAtPresent = -1
    rankAtPresentArr = list()

    rankOfAllScores = getInitRank(scores)

    i, j = len(scores)-1, 0
    # print("i, j =",i, j)
    # print(scores)
    # print(rankOfAllScores)
    while(1):
        if i == 0:
            if newPlayersScores[j] >= scores[i]:
                if newPlayersScores[j] > scores[i]:
                    rankAtPresent = rankOfAllScores[0]-1
                else:
                    rankAtPresent = rankOfAllScores[0]
                # rankAtPresent = 1#rankOfAllScores[0]
                
                rankAtPresentArr.append(rankAtPresent)
                rankOfAllScores = [rankAtPresent] + [k+1 for k in rankOfAllScores]
                
                
                scores = [newPlayersScores[j]] + scores
                # rankAtPresentArr.append(sorted(list(set(scores)),reverse=True).index(newPlayersScores[j])+1)
                j += 1
            else:
                i -= 1
        
        elif i == len(scores)-1:
            if newPlayersScores[j] <= scores[i]:
                if newPlayersScores[j] < scores[i]:
                    rankAtPresent = rankOfAllScores[-1]+1
                else:
                    rankAtPresent = rankOfAllScores[-1]

                rankAtPresentArr.append(rankAtPresent)
                rankOfAllScores = rankOfAllScores + [rankAtPresent]

                scores = scores + [newPlayersScores[j]]
                # rankAtPresentArr.append(sorted(list(set(scores)),reverse=True).index(newPlayersScores[j])+1)
                j += 1
                
            else:
                i -= 1
        else:
            
            if newPlayersScores[j] <= scores[i-1] and newPlayersScores[j] >= scores[i]:
                if newPlayersScores[j] == scores[i-1]:
                    # rankAtPresent = rankOfAllScores[:i-1][-1]
                    rankAtPresent = rankOfAllScores[i-1]
                    rankOfAllScores = rankOfAllScores[:i-1]+ [rankAtPresent] + [k+1 for k in rankOfAllScores[i-1:]]
                elif newPlayersScores[j] == scores[i]:
                    rankAtPresent = rankOfAllScores[i:][0]
                    rankOfAllScores = rankOfAllScores[:i]+ [rankAtPresent] + [k+1 for k in rankOfAllScores[i:]]
                elif newPlayersScores[j] < scores[i-1] and newPlayersScores[j] > scores[i]:
                    rankAtPresent = rankOfAllScores[:i][-1]+1
                    rankOfAllScores = rankOfAllScores[:i]+ [rankAtPresent] + [k+1 for k in rankOfAllScores[i:]]   

                rankAtPresentArr.append(rankAtPresent)

                scores = scores[:i] + [newPlayersScores[j]] + scores[i:]
                # rankAtPresentArr.append(sorted(list(set(scores)),reverse=True).index(newPlayersScores[j])+1)
                j += 1
            
            else:
                i -= 1

        
        if j == len(newPlayersScores):
            break

        # print("i, j =",i, j)
        # print(scores)
        # print(rankOfAllScores)
        print([1 if i < 1 else i for i in rankAtPresentArr])
        
    # if rankAtPresentArr[-1] < 1:
    #     # c = rankAtPresentArr[-1]*-1 + 1
    #     return [i+rankAtPresentArr[-1]*-1 + 1  for i in rankAtPresentArr]
    # else:
    #     return rankAtPresentArr
    return [1 if i < 1 else i for i in rankAtPresentArr]

scores, newPlayersScores = [100, 90, 90, 80, 80, 80, 75, 60], [50, 65, 77, 90, 122]
customInput =   '''
                7
                100 100 50 40 40 20 10
                8
                5 25 50 120 180 190 190 200
                '''
scores, newPlayersScores = [100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120, 180, 190, 190, 200]
scores, newPlayersScores = [100, 100, 50, 40, 40, 20, 10], [1, 2, 3, 5, 25, 50, 120]
# scores, newPlayersScores = [295, 294, 291, 287, 287, 285, 285, 284, 283, 279, 277, 274, 274, 271, 270, 268, 268, 268, 264, 260, 259, 258, 257, 255, 252, 250, 244, 241, 240, 237, 236, 236, 231, 227, 227, 227, 226, 225, 224, 223, 216, 212, 200, 197, 196, 194, 193, 189, 188, 187, 183, 182, 178, 177, 173, 171, 169, 165, 143, 140, 137, 135, 133, 130, 130, 130, 128, 127, 122, 120, 116, 114, 113, 109, 106, 103, 99, 92, 85, 81, 69, 68, 63, 63, 63, 61, 57, 51, 47, 46, 38, 30, 28, 25, 22, 15, 14, 12, 6, 4], [5, 5, 6, 14, 19, 20, 23, 25, 29, 29, 30, 30, 32, 37, 38, 38, 38, 41, 41, 44, 45, 45, 47, 59, 59, 62, 63, 65, 67, 69, 70, 72, 72, 76, 79, 82, 83, 90, 91, 92, 93, 98, 98, 100, 100, 102, 103, 105, 106, 107, 109, 112, 115, 118, 118, 121, 122, 122, 123, 125, 125, 125, 127, 128, 131, 131, 133, 134, 139, 140, 141, 143, 144, 144, 144, 144, 147, 150, 152, 155, 156, 160, 164, 164, 165, 165, 166, 168, 169, 170, 171, 172, 173, 174, 174, 180, 184, 187, 187, 188, 194, 197, 197, 197, 198, 201, 202, 202, 207, 208, 211, 212, 212, 214, 217, 219, 219, 220, 220, 223, 225, 227, 228, 229, 229, 233, 235, 235, 236, 242, 242, 245, 246, 252, 253, 253, 257, 257, 260, 261, 266, 266, 268, 269, 271, 271, 275, 276, 281, 282, 283, 284, 285, 287, 289, 289, 295, 296, 298, 300, 300, 301, 304, 306, 308, 309, 310, 316, 318, 318, 324, 326, 329, 329, 329, 330, 330, 332, 337, 337, 341, 341, 349, 351, 351, 354, 356, 357, 366, 369, 377, 379, 380, 382, 391, 391, 394, 396, 396, 400]
# print("expected output")
# print([88, 88, 87, 85, 84, 84, 83, 82, 81, 81, 80, 80, 80, 80, 79, 79, 79, 79, 79, 79, 79, 79, 77, 75, 75, 74, 73, 73, 73, 71, 71, 71, 71, 71, 71, 70, 70, 69, 69, 68, 68, 68, 68, 67, 67, 67, 66, 66, 65, 65, 64, 64, 62, 61, 61, 60, 59, 59, 59, 59, 59, 59, 58, 57, 56, 56, 55, 55, 53, 52, 52, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 50, 50, 50, 50, 49, 49, 48, 48, 47, 47, 47, 45, 43, 42, 42, 41, 38, 36, 36, 36, 36, 35, 35, 35, 35, 35, 35, 34, 34, 34, 33, 33, 33, 33, 33, 32, 30, 28, 28, 28, 28, 27, 27, 27, 26, 23, 23, 22, 22, 20, 20, 20, 18, 18, 15, 15, 14, 14, 13, 13, 11, 11, 10, 10, 8, 8, 7, 6, 5, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
print(climbingLeaderboard(scores, newPlayersScores))
# print(list(dict.fromkeys(scores))[::-1])