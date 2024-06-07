# class Solution:
#     def removeElement(self, nums: list, val: int) -> int:
#         c = len(nums)
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 nums[i] = '_'
#                 c -= 1
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[j] == '_':
#                     nums[i], nums[j] = nums[j], nums[i]
#         return c
class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        curr = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[curr] = nums[i]
                curr += 1
        return curr
f = Solution()
print(f.removeElement(nums=[3, 2, 2, 3], val=3))
print(f.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
print(f.removeElement(nums=[45, 51, 2, 2, 62, 2, 3, 6, 84, 2, 2, 72], val=2))
print(f.removeElement(nums=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], val=2))
