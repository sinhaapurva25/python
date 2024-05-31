class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)
        elif target == nums[0]:
            return 0
        elif target == nums[len(nums) - 1]:
            return len(nums) - 1
        else:
            i = 1
            while i < len(nums):
                if target == nums[i]:
                    return i
                elif nums[i - 1] <= target < nums[i]:
                    return i
                i += 1
        return -1

f = Solution()
print(f.searchInsert([1, 3, 5, 6], 2))

# Next challenges:
# First Bad Version
# Minimum Operations to Exceed Threshold Value I
