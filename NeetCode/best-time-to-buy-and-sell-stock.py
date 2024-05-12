class Solution:
    def maxProfit(self, prices: list) -> int:
        mx = 0
        for i in range(len(prices)-1, -1, -1):
            for j in range(i-1, -1, -1):
                # print(prices[i], prices[j], prices[i]-prices[j])
                diff = prices[i] - prices[j]
                if prices[i] - prices[j] > 0 and prices[i] - prices[j] > mx:
                        mx = prices[i] - prices[j]
            # print()
        return mx
s = Solution()
print(s.maxProfit(prices = [7,1,5,3,6,4]))
print(s.maxProfit(prices = [7,6,4,3,1]))