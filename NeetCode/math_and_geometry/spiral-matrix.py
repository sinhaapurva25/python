class Solution:
    def spiralOrder(self, matrix: list) -> list:
        res = list()
        m = len(matrix)
        n = len(matrix[0])
        if m >= n:
            pass
            print('here')
        else:
            j = 0
            for i in range(min(m, n)//2):
                r = i
                for c in range(j, n-j):
                    # res.append(matrix[r][c])
                    print([r][c])
                c = n-j-1
                for r in range(i+1, m-(i+1)):
                    # res.append(matrix[r][c])
                    print([r][c])
                r = m-i
                for c in range(n-j-1,j-1,-1):
                    # res.append(matrix[r][c])
                    print([r][c])
                c = j
                # for r in range(m-(i+1)-1, i, 1):
                for r in range(m-i, i, 1):
                    # res.append(matrix[r][c])
                    print([r][c])
                j += 1

        return res
f = Solution()
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# f.spiralOrder(matrix)
# print(matrix)
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
f.spiralOrder(matrix)
print(matrix)