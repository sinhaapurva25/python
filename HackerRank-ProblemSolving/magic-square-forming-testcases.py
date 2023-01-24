import math
import os
import random
import re
import sys
import copy
# import numpy as np

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def checkOrder(i,res,ms1,ms2):
    if i == len(ms1):
        return res
    else:
        i += 1
        res.append([ms1[(j+i)%len(ms1)] for j in range(len(ms1))])
        res.append([ms2[(j+i)%len(ms2)] for j in range(len(ms2))])
        return checkOrder(i,res,ms1,ms2)

# def sum_2DArr(ms):
#     return sum([sum(i) for i in ms]), np.sum(np.sum(np.array(ms), axis = 0))

def formingMagicSquare(s):
    
    n = 3
    magic_constant = n*(n*n+1)//2
    mid = magic_constant//3

    count = 0

    if s[n//2][n//2]!= mid:
        count += s[n//2][n//2]-mid if s[n//2][n//2] > mid else mid-s[n//2][n//2]
        s[n//2][n//2] = mid
    
    perms_even = checkOrder(0,[],[2, 4, 8, 6],[2, 6, 8, 4])
    perms_odd = checkOrder(0,[],[9, 3, 1, 7], [7, 1, 3, 9])
    
    minimumArr = []
    for p in range(len(perms_even)):

        ms = copy.deepcopy(s)

        ms[0][0], ms[n-1][0], ms[n-1][n-1], ms[0][n-1] = perms_even[p][0], perms_even[p][1], perms_even[p][2], perms_even[p][3]
        ms[n//2][0], ms[n-1][n//2], ms[n//2][n-1], ms[0][n//2] = perms_odd[p][0], perms_odd[p][1], perms_odd[p][2], perms_odd[p][3]
        
        ch = 0
        for i in range(n):
            for j in range(n):
                diff = ms[i][j] - s[i][j] if (ms[i][j] >= s[i][j]) else s[i][j] - ms[i][j]
                ch += diff

        minimumArr.append(ch)
        '''
        [print(m) for m in ms]
        print('-----')
        print(sum_2DArr(ms))
        '''
    
    count += min(minimumArr)
    return count
	
print(formingMagicSquare([[4,9,2], [3,5,7], [8,1,5]]))
print(formingMagicSquare([[4,8,2], [4,5,7], [6,1,6]]))