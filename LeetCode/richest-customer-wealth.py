class Solution:
    def maximumWealth(self, accounts: list()) -> int:
        mx = float("-inf")
        for i in accounts:
            if sum(i) > mx: mx = sum(i)
        return mx
s = Solution()
s.maximumWealth([[1,2,3],[3,2,1]])
s.maximumWealth([[1,5],[7,3],[3,5]])
s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])