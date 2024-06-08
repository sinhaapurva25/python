class Solution:
    def maxSubArray(self, nums: list) -> int:
        max_sum = float("-inf")
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum > max_sum:
                max_sum = current_sum

            if current_sum < 0:
                current_sum = 0
        return max_sum

s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(nums))
