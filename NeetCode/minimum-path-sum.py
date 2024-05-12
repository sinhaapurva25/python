class Solution:
    def minPathSum(self, grid) -> int:
        sum_rows = list()
        sum_columns = list()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            sum_rows.append(sum(grid[i]))
        for i in range(n):
            sum_columns.append(sum([grid[j][i] for j in range(n)]))
        print(sum_rows, sum_columns)


s = Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

