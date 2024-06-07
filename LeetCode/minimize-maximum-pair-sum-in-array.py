class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        mx = float("-inf")
        for i in range(len(nums) // 2):
            if nums[i] + nums[len(nums) - i - 1] > mx:
                mx = nums[i] + nums[len(nums) - i - 1]
        return mx


f = Solution()
print(f.minPairSum([3, 5, 4, 2, 4, 6]))
# Next challenges:
# Find the Celebrity
# 01 Matrix
# Find the String with LCP