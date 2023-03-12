# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#         res = list()
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     res.extend([i, j])
#         return res
# Runtime: 4014 ms, Beats: 14.58%
# Memory: 14.9 MB; Beats: 91.28%


# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#         N = len(nums)
#
#         for i in range(N):
#             to_find = target - nums[i]
#             try:
#                 idx = nums.index(to_find, i + 1, N)
#             except ValueError:
#                 idx = -1
#             if idx > -1 and idx != i:
#                 return [i, idx]
# Runtime: 548 ms; Beats: 41.26%
# Memory: 14.9 MB; Beats: 91.28%

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        dct = {}
        N = len(nums)
        for i in range(N):
            if nums[i] in dct:
                return [i, dct[nums[i]]]
            else:
                dct[target - nums[i]] = i


# Runtime: 62 ms; Beats: 76.65%
# Memory: 15.4 MB; Beats 6.13%
''' HeapSort followed by binary Search won't work,
because you will end up changing the original indices nums '''
f = Solution()
print(f.twoSum(nums=[2, 7, 11, 15], target=9))
print(f.twoSum(nums=[3, 2, 4], target=6))
print(f.twoSum(nums=[3, 3], target=6))
print(f.twoSum(nums=[-1, 1], target=0))
print(f.twoSum(nums=[-1, -1], target=0))
print(f.twoSum(nums=[-1, 3], target=0))
print(f.twoSum(nums=[-1, 3, 1], target=4))
print(f.twoSum(nums=[-1, 3, 1, 4, 0], target=4))
