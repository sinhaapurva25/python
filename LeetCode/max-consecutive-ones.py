class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        first_occ_of_1 = None
        for i in nums:
            if i == 1:
                first_occ_of_1 = i
        if first_occ_of_1 is None:
            return 0

        res = [[0, 0]]
        len_of_longest_subsequence = 0
        for i in range(1, len(nums)):
            if nums[i] == 1 and nums[i-1] == 1:
                res[len(res)-1][1] += 1
            else:
                res.append([i, i])
            if res[len(res)-1][1] - res[len(res)-1][0] > len_of_longest_subsequence:
                len_of_longest_subsequence = res[len(res)-1][1] - res[len(res)-1][0]
        return len_of_longest_subsequence+1

s = Solution()
# print(s.findMaxConsecutiveOnes([1, 1, 0, 1]))
print(s.findMaxConsecutiveOnes([0]))
print(s.findMaxConsecutiveOnes([0, 0, 0, 1]))