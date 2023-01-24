#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, kkkkkkk):
    r = len(matrix)//2 if len(matrix)%2==0 else len(matrix)//2+1
    c = len(matrix[0])//2 if len(matrix[0])%2==0 else len(matrix[0])//2+1
    # print(r,c)
    layers = [[] for i in range(min(r,c))]
    res_arr = matrix.copy()

    rows = 0
    cols = 1
    l = 0
    while l!=min(r,c):
    # while rows!=r and cols!=c:
        # print(rows,m-rows,cols,n-cols)# print(rows,m-rows-1,cols,n-cols-1)
        left = [matrix[j][rows]for j in range(rows,m-rows)]
        bottom = [matrix[m-rows-1][i]for i in range(cols,n-cols)]
        right = [matrix[j][n-cols]for j in range(m-rows-1,rows-1,-1)]
        top = [matrix[rows][i] for i in range(n-cols-1,cols-1,-1)]
        indices = [[j,rows] for j in range(rows,m-rows)] + [[m-rows-1,i] for i in range(cols,n-cols)] + [[j,n-cols] for j in range(m-rows-1,rows-1,-1)] + [[rows,i] for i in range(n-cols-1,cols-1,-1)]
        layers[l].extend(left)
        layers[l].extend(bottom)
        layers[l].extend(right)
        layers[l].extend(top)
        # print(layers)
        # print(len(layers[l]),len(indices))
        
        rotated_arr = [layers[l][(i-kkkkkkk)%len(layers[l])] for i in range(len(layers[l]))]
        
        for i in range(len(layers[l])):
            res_arr[indices[i][0]][indices[i][1]] = rotated_arr[i]
        rows += 1
        cols += 1
        l += 1
    # [print(i) for i in res_arr]
    res = ''
    for i in res_arr:
        for j in i:
            res += str(j)+' '
        res+='\n'
    print(res)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
