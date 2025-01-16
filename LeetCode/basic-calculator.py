from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mn = float("inf")
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if sum(nums[i:j]) >= target:
                    if j - i < mn:
                        mn = j - i
        if mn == float("inf"):
            return 0
        return mn

s = Solution()
print(s.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(target=4, nums=[1, 4, 4]))
print(s.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
print(s.minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5]))
