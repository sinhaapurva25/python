class Solution:
    def binary_search(self, nums, target, start, end):
        mid = (start + end) // 2
        if mid < 0 or mid > len(nums) - 1 or start > end:
            return -1

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid - 1
            if nums[0] < target: return start
            if len(nums) > 1: return self.binary_search(nums, target, start, end)

        else:
            start = mid + 1
            if nums[len(nums)-1] < target: return end
            if len(nums) > 1: return self.binary_search(nums, target, start, end)

    def searchInsert(self, nums: list, target: int) -> int:
        start = 0
        end = len(nums)-1


        binary_search(nums, target, start, end)