class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # nums.sort()
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        s = nums[0]
        max_s = nums[0]

        for i in range(1, len(nums)):
            s += nums[i]
            if s > max_s:
                max_s = s

        s = nums[-1]
        for i in range(1, len(nums)):
            s += nums[len(nums)-i-1]
            if s > max_s:
                max_s = s
        return max_s