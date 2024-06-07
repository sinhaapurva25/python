class Solution:
    def maxProfit(self, prices: list) -> int:
        # mx = 0
        # for i in range(len(prices)-1, -1, -1):
        #     for j in range(i-1, -1, -1):
        #         diff = prices[i] - prices[j]
        #         if diff > 0 and diff > mx:
        #             mx = diff
        # return mx
        mx, mn = 0, float("inf")
        for i in range(len(prices)):
            if prices[i] < mn:
                mn = prices[i]
            elif prices[i] - mn > mx:
                mx = prices[i] - mn
        return mx
s = Solution()
print(s.maxProfit(prices = [7,1,5,3,6,4]))
print(s.maxProfit(prices = [7,6,4,3,1]))