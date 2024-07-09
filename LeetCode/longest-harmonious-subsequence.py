from typing import List


# class Solution:
#     def findLHS(self, nums: List[int]) -> int:
#         freq = dict()
#         for i in range(len(nums)):
#             if nums[i] in freq:
#                 freq[nums[i]][1] = i
#             else:
#                 freq[nums[i]] = [i, i]
#
#         mx = float("-inf")
#         for k in freq.keys():
#             if k - 1 in freq:
#                 l = freq[k][1] - freq[k - 1][0] + 1
#                 if l > mx:
#                     mx = l
#
#         if mx == float("-inf"):
#             return 0
#         return mx

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = dict()
        for i in range(len(nums)):
            freq[nums[i]] = 1+freq.get(nums[i], 0)
        mx = 0
        for num in freq.keys():
            if num+1 in freq:
                if freq[num] + freq[num+1] > mx:
                    mx = freq[num] + freq[num+1]
        return mx

s = Solution()
print(s.findLHS(nums=[1, 3, 2, 2, 5, 2, 3, 4, 7]))
print(s.findLHS(nums=[1, 3, 2, 2, 5, 2, 3, 7]))
print(s.findLHS(nums=[1, 2, 3, 4]))
print(s.findLHS(nums=[1, 1, 1, 1]))
