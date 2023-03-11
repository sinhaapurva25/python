class Solution:
    def swap_elements_in_2D_matrix(self, matrix, i, j):
        if i!=j:
            matrix[i][j] ^= matrix[j][i]
            matrix[j][i] ^= matrix[i][j]
            matrix[i][j] ^= matrix[j][i]
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = (len(matrix))
        if n > 1:
            for i in range(n-1):
                for j in range(i+1, n):
                    self.swap_elements_in_2D_matrix(matrix, i, j)
            for i in range(n):
                for j in range(n//2):
                    matrix[i][j],matrix[i][n - j - 1] = matrix[i][n - j - 1],matrix[i][j]

f = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
f.rotate(matrix)
print(matrix)
import numpy as np
np.random.seed(7)
matrix = [[int(np.random.rand() * 10) for i in range(1, 6)] for j in range(1, 6)]
f.rotate(matrix)
print(matrix)
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
f.rotate(matrix)
print(matrix)