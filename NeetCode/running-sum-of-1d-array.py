class Solution:
    def runningSum(self, nums: list()) -> list():
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

s = Solution()
s.runningSum([1,2,3,4])
s.runningSum([1,1,1,1,1])
s.runningSum([3,1,2,10,1])