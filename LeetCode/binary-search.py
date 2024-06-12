class Solution:
    def binary_search(self, nums, target, s, e):
        mid = (s + e) // 2
        if mid < 0 or mid > len(nums) - 1 or s > e:
            return -1
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            s = mid + 1
            return self.binary_search(nums, target, s, e)
        else:
            e = mid - 1
            return self.binary_search(nums, target, s, e)

    def search(self, nums: list, target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums))



s = Solution()
nums = [-1, 0, 3, 5, 9, 12]
print(s.search(nums, 9))
