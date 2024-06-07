class Solution:
    def longestConsecutive(self, nums: list) -> int:

        nums = sorted(list(set(nums)))
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        dct = dict()
        dct[0] = [0, 0]
        c = 0
        len_of_longest_seq = 0
        for i in range(1, len(nums)):
            if 0 <= nums[i] - nums[i - 1] <= 1:
                dct[c][1] = i
            else:
                c += 1
                dct[c] = [i, i]
            if dct[c][1] - dct[c][0] > len_of_longest_seq:
                len_of_longest_seq = dct[c][1] - dct[c][0]
        return len_of_longest_seq+1


s = Solution()
print(s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(s.longestConsecutive(nums=[1, 2, 0, 1]))
print(s.longestConsecutive(nums=[0]))
print(s.longestConsecutive(nums=[0, 0]))
print(s.longestConsecutive(nums=[]))
print(s.longestConsecutive(nums=[28, 26, 27, 40, 80, 81, 42, 44, 45, 41, 42, 43]))
print(s.longestConsecutive(nums=[28, 26, 27, 40, 80, 81, 42, 44, 45, 41, 43]))
