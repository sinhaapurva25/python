class Solution:
    def getRow(self, rowIndex: int):
        pascals_triangle = [[1], [1,1]]
        if rowIndex >= 2:
            for i in range(2, rowIndex + 1):
                row = [1]
                prev_rowIndex = pascals_triangle[i-1]
                for j in range(1, i):
                    row.append(prev_rowIndex[j-1] + prev_rowIndex[j])
                row.append(1)
                pascals_triangle.append(row)
        return pascals_triangle[rowIndex]

s = Solution()
print(s.getRow(3))
print(s.getRow(4))
print(s.getRow(5))