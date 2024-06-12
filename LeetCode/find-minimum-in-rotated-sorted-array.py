class Solution:
    def findMin(self, nums: list) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < nums[right]:
                # it means from left to mid, numbers are arranged in ascending order and you need to concentrate from mid to right
                right = mid
                # close the gap between md and right
            else:
                left = mid + 1
        return nums[right]


s = Solution()
print(s.findMin(nums=[3, 4, 5, 1, 2]))
print(s.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
print(s.findMin(nums=[11, 13, 15, 17]))
print(s.findMin(nums=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(s.findMin(nums=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

# Next challenges:
# Search in Rotated Sorted Array
# Find Minimum in Rotated Sorted Array II

# you spent two days on this problem
# Spent time and dry ran the following examples to finally make sense:
# [6, 7, 0, 1, 2] and [2, 3, 4, 5, 6, 7, 8, 9, 0]
# Find solution for getting the max element in [0, 9, 8, 7, 6, 5, 4, 3, 2, 1] -> arr[left] < arr[mid]