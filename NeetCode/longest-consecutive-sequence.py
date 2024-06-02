class BruteForceSolution:
    def longestConsecutive(self, nums: list):
        nums = list(set(nums))
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        mx = float('-inf')
        c = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                c += 1
                if c > mx:
                    mx = c
            else:
                c = 1

        return mx

from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: list):
        nums = list(set(nums))
        dct = defaultdict(int)
        for i in nums:
            dct[i] = 1
        res_dict = dct
        for k in dct.keys():
            print(k - 1, res_dict[res_dict[k - 1]])
            # print(dct[k - 1] == 0)
        print(dct)

f = BruteForceSolution()

class Solution:
    def longestConsecutive(self, nums: list) -> int:

        if len(nums) < 1:
            return 1
        nums.sort()
        # diff_nums = [None] * (len(nums) - 1)
        # for i in range(len(nums) - 1):
        #     diff_nums[i] = nums[i + 1] - nums[i]
        # print(diff_nums)
        # print(dict([1, 2, 3]))
        # return 0

        present_largest_subsequence = 0
        largest_subsequence = 0
        for i in range(len(nums)):
            if i != 0:
                if nums[i] == 1 and nums[i-1] == 1:
                    present_largest_subsequence += 1
                    if present_largest_subsequence > largest_subsequence:
                        largest_subsequence = present_largest_subsequence
                else:
                    present_largest_subsequence = 0
                    
        return largest_subsequence

s = Solution()
print(s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
# print(s.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
# print(s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
# print(s.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
# print(s.longestConsecutive(nums=[1, 2, 0, 1]))
# print(s.longestConsecutive(nums=[0]))
# print(s.longestConsecutive(nums=[0, 0]))
# print(s.longestConsecutive(nums=[]))
