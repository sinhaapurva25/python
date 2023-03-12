class Solution:
    def spiralOrder(self, matrix: list) -> list:

        m = len(matrix)
        n = len(matrix[0])
        if m==1 or n==1:
            if m == 1:
                return matrix[0]
            else:
                return [i[0] for i in matrix]

        res = list()
        j = 0
        for i in range(min(m, n)//2):
            r = i
            for c in range(j, n-j):
                res.append(matrix[r][c])
            c = n-j-1
            for r in range(i+1, m-i-1):
                res.append(matrix[r][c])
            r = m-i-1
            for c in range(n-j-1,j-1,-1):
                res.append(matrix[r][c])
            c = j
            for r in range(m-i-1-1, i, -1):
                res.append(matrix[r][c])
            j += 1

        if len(res) < m*n:
            if m >= n:
                j = n//2
                for i in range(j, m-n//2):
                    res.append(matrix[i][j])
                # print(f'm={m},n={n} m>n is True')
            else:
                i = m//2
                for j in range(i, n-m//2):
                    res.append(matrix[i][j])
                # print(f'm={m},n={n} m>n is False')
        return res


f = Solution()

import numpy as np

np.random.seed(7)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[print(i) for i in matrix]
print(len(f.spiralOrder(matrix)), f.spiralOrder(matrix))
print('----------')

print('here')
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
[print(i) for i in matrix]
print(len(f.spiralOrder(matrix)), f.spiralOrder(matrix))
print('----------')

matrix = [[int(np.random.rand() * 10) for i in range(9)] for j in range(5)]
[print(i) for i in matrix]
f.spiralOrder(matrix)
print(len(f.spiralOrder(matrix)), f.spiralOrder(matrix))
print('----------')
print('here-end')

matrix = [[int(np.random.rand() * 10) for i in range(3)] for j in range(4)]
[print(i) for i in matrix]
f.spiralOrder(matrix)
print(len(f.spiralOrder(matrix)), f.spiralOrder(matrix))
print('----------')

matrix = [[int(np.random.rand() * 10) for i in range(4)] for j in range(4)]
[print(i) for i in matrix]
f.spiralOrder(matrix)
print(len(f.spiralOrder(matrix)), f.spiralOrder(matrix))
print('----------')

matrix = [[int(np.random.rand() * 10) for i in range(4)] for j in range(6)]
[print(i) for i in matrix]
f.spiralOrder(matrix)
print(len(f.spiralOrder(matrix)), f.spiralOrder(matrix))
print('----------')

matrix = [[int(np.random.rand() * 10) for i in range(3)] for j in range(3)]
[print(i) for i in matrix]
f.spiralOrder(matrix)
print(len(f.spiralOrder(matrix)), f.spiralOrder(matrix))
print('----------')

matrix = [[int(np.random.rand() * 10) for i in range(3)] for j in range(7)]
[print(i) for i in matrix]
f.spiralOrder(matrix)
print(len(f.spiralOrder(matrix)), f.spiralOrder(matrix))
print('----------')

matrix = [[int(np.random.rand() * 10) for i in range(7)] for j in range(3)]
[print(i) for i in matrix]
f.spiralOrder(matrix)
print(len(f.spiralOrder(matrix)), f.spiralOrder(matrix))
print('----------')

matrix = [[int(np.random.rand() * 10) for i in range(7)] for j in range(7)]
[print(i) for i in matrix]
f.spiralOrder(matrix)
print(len(f.spiralOrder(matrix)), f.spiralOrder(matrix))
print('----------')

matrix = [[int(np.random.rand() * 10) for i in range(3)] for j in range(7)]
[print(i) for i in matrix]
f.spiralOrder(matrix)
print(len(f.spiralOrder(matrix)), f.spiralOrder(matrix))
print('----------')
