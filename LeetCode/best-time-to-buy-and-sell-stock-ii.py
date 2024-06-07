class Solution:
    def maxProfit(self, prices: list) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                res += prices[i] - prices[i-1]
        return res

f = Solution()
print(f.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(f.maxProfit(prices=[1, 2, 3, 4, 5]))
