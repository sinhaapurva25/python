class Solution:
    def shiftGrid(self, grid: list, k: int) -> list:
        m, n = len(grid), len(grid[0])
        for c in range(k):
            l = grid[m - 1][n - 1]
            for i in range(m):
                for j in range(n):
                    t = grid[i][j]
                    grid[i][j] = l
                    l = t
        return grid
f = Solution()
print(f.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], k = 1))
print(f.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))