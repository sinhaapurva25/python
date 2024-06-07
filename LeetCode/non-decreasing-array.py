class Solution:
    def checkPossibility(self, nums: list) -> bool:
        print(nums)
        if len(nums) <= 1:
            return True
        else:
            for i in range(1, len(nums)-1):
                if nums[i-1] > 1:
                    return False
        return True

s = Solution()
print(s.checkPossibility([4,2,3]))
print(s.checkPossibility([4,2,1]))
