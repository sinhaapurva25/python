class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix[i])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = ''
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = ''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '':
                    matrix[i][j] = 0
f = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
f.setZeroes(matrix)
print(matrix)
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
f.setZeroes(matrix)
print(matrix)