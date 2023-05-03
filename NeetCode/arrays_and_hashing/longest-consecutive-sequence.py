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
# f = Solution()
# print(f.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
# print(f.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
# print(f.longestConsecutive(nums=[1, 2, 0, 1]))
# print(f.longestConsecutive(nums=[0]))
# print(f.longestConsecutive(nums=[0, 0]))
# print(f.longestConsecutive(nums=[]))
print(f.longestConsecutive(nums=[-6,-1,-1,9,-8,-6,-6,4,4,-3,-8,-1]))
