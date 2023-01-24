#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    for i in grid: print(i)
    row_size = 0
    col_size = 0
    for i in grid:
        col_size = 0
        for j in i:
            col_size += 1
        row_size += 1
    # print(row_size,col_size)
    result = 0
    row_idx = 0
    for row in grid:
        col_idx = 0
        for col in row:
            if row_idx == 0 and col_idx == 0:  # print(row_idx, col_idx, 'left-top')
                if col > grid[row_idx][col_idx + 1] and col > grid[row_idx + 1][col_idx] and col > grid[row_idx + 1][
                    col_idx + 1]:
                    result += 1
            if row_idx == 0 and col_idx == col_size - 1:  # print(row_idx, col_idx, 'right-top')
                if col > grid[row_idx][col_idx - 1] and col > grid[row_idx - 1][col_idx - 1] and col > \
                        grid[row_idx + 1][col_idx]:
                    result += 1
            if row_idx == row_size - 1 and col_idx == 0:  # print(row_idx, col_idx, 'left-bottom')
                if col > grid[row_idx - 1][col_idx] and col > grid[row_idx - 1][col_idx + 1] and col > grid[row_idx][
                    col_idx + 1]:
                    result += 1
            if row_idx == row_size - 1 and col_idx == col_size - 1:  # print(row_idx, col_idx, 'right-bottom')
                if col > grid[row_idx - 1][col_idx - 1] and col > grid[row_idx - 1][col_idx] and col > grid[row_idx][
                    col_idx - 1]:
                    result += 1
            if row_idx == 0 and 0 < col_idx < col_size - 1:  # print(row_idx, col_idx, 'top row')
                if (col > grid[row_idx][col_idx - 1] and
                        col > grid[row_idx][col_idx + 1] and
                        col > grid[row_idx + 1][col_idx - 1] and
                        col > grid[row_idx + 1][col_idx] and
                        col > grid[row_idx + 1][col_idx + 1]):
                    result += 1
            if row_idx == row_size - 1 and 0 < col_idx < col_size - 1:  # print(row_idx, col_idx, 'bottom row')
                if (col > grid[row_idx - 1][col_idx - 1] and
                        col > grid[row_idx - 1][col_idx] and
                        col > grid[row_idx - 1][col_idx + 1] and
                        col > grid[row_idx][col_idx - 1] and
                        col > grid[row_idx][col_idx + 1]):
                    result += 1
            if 0 < row_idx < row_size - 1 and col_idx == 0:  # print(row_idx, col_idx, 'left column')
                if (col > grid[row_idx - 1][col_idx] and
                        col > grid[row_idx - 1][col_idx + 1] and
                        col > grid[row_idx][col_idx + 1] and
                        col > grid[row_idx + 1][col_idx] and
                        col > grid[row_idx + 1][col_idx + 1]):
                    result += 1
            if 0 < row_idx < row_size - 1 and col_idx == col_size - 1:  # print(row_idx, col_idx, 'right column')
                if (col > grid[row_idx - 1][col_idx - 1] and
                        col > grid[row_idx - 1][col_idx] and
                        col > grid[row_idx][col_idx - 1] and
                        col > grid[row_idx + 1][col_idx - 1] and
                        col > grid[row_idx + 1][col_idx]):
                    result += 1
            elif 0 < row_idx < row_size - 1 and 0 < col_idx < col_size - 1:
                if (col > grid[row_idx - 1][col_idx - 1] and
                        col > grid[row_idx - 1][col_idx] and
                        col > grid[row_idx - 1][col_idx + 1] and
                        col > grid[row_idx][col_idx - 1] and
                        col > grid[row_idx][col_idx + 1] and
                        col > grid[row_idx + 1][col_idx - 1] and
                        col > grid[row_idx + 1][col_idx] and
                        col > grid[row_idx + 1][col_idx + 1]):
                    result += 1
                # print(col)
            col_idx += 1
        row_idx += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()