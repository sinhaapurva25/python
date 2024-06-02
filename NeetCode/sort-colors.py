class Solution:

    # def sortColors(self, nums: list) -> None:
    #     i = 0
    #     j = 0
    #     k = 0
    #
    #     for _ in nums:
    #         if _ == 0:
    #             i += 1
    #         elif _ == 1:
    #             j += 1
    #         else:
    #             k += 1
    #
    #     j += i
    #     k += j
    #
    #     _ = 0
    #     while _ < i:
    #         nums[_] = 0
    #         _ += 1
    #     while _ < j:
    #         nums[_] = 1
    #         _ += 1
    #     while _ < k:
    #         nums[_] = 2
    #         _ += 1

    def sortColors(self, nums: list) -> None:
        freq = dict()
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        res_duplicate = list()
        if 0 in freq.keys():
            res_duplicate.extend([0] * freq[0])
        if 1 in freq.keys():
            res_duplicate.extend([1] * freq[1])
        if 1 in freq.keys():
            res_duplicate.extend([2] * freq[2])
        for idx, num in enumerate(res_duplicate):
            nums[idx] = num

f = Solution()
nums = [2, 0, 2, 1, 1, 0]
f.sortColors(nums)
print(nums)
nums = [2, 0, 2, 1, 1, 0, 0, 2, 2, 2, 1]
f.sortColors(nums)
print(nums)
nums = [2, 0, 1]
f.sortColors(nums)
print(nums)
