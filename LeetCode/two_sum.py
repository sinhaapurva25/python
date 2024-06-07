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
        dct = dict()
        res = list()
        for i, v in enumerate(nums):
            diff = target - v
            if diff in dct:
                res.append([dct[diff], i])
            dct[v] = i
        return res


# Runtime: 62 ms; Beats: 76.65%
# Memory: 15.4 MB; Beats 6.13%
''' HeapSort followed by binary Search won't work,
because you will end up changing the original indices nums '''
f = Solution()
# print(f.twoSum(nums=[2, 7, 11, 15], target=9))
# print(f.twoSum(nums=[3, 2, 4], target=6))
# print(f.twoSum(nums=[3, 3], target=6))
# print(f.twoSum(nums=[-1, 1], target=0))
# print(f.twoSum(nums=[-1, -1], target=0))
# print(f.twoSum(nums=[-1, 3], target=0))
# print(f.twoSum(nums=[-1, 3, 1], target=4))
# print(f.twoSum(nums=[-1, 3, 1, 4, 0], target=4))
print(f.twoSum(nums=[1, 0, 1, -1, 3, -1, 0, -2, 2, -1, -3, 1, -2, 2, 0], target=0))

# Next challenges:
# 3Sum
# 4Sum
# Two Sum II - Input Array Is Sorted
# Two Sum III - Data structure design
# Subarray Sum Equals K
# Two Sum IV - Input is a BST
# Two Sum Less Than K
# Max Number of K-Sum Pairs
# Count Good Meals
# Count Number of Pairs With Absolute Difference K
# Number of Pairs of Strings With Concatenation Equal to Target
# Find All K-Distant Indices in an Array
# First Letter to Appear Twice
# Number of Excellent Pairs
# Number of Arithmetic Triplets
# Node With Highest Edge Score
# Check Distances Between Same Letters
# Find Subarrays With Equal Sum
# Largest Positive Integer That Exists With Its Negative
# Number of Distinct Averages
# Count Pairs Whose Sum is Less than Target
