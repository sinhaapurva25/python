class Solution:
    def maxArea(self, height: list) -> int:
        # BRUTE FORCE
        # mx = 0
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         area = (j-i) * (min(height[i], height[j]) if height[i] != height[j] else height[i])
        #         if area > mx:
        #             mx = area
        #             print(j, i, (min(height[i], height[j]) if height[i] != height[j] else height[i]))
        # return mx
        mx = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = (j-i) * (min(height[i], height[j]) if height[i] != height[j] else height[i])
            if area > mx:
                mx = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return mx


s = Solution()
print("result", s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print("result", s.maxArea([1,1]))
print("result", s.maxArea([4,3,2,1,4]))
# Next challenges:
# Trapping Rain Water
# Maximum Tastiness of Candy Basket
# House Robber IV
