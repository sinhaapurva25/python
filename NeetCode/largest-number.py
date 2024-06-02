class Solution:
    def largestNumber(self, nums: list) -> str:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
                    nums[i] ^= nums[j]
                    nums[j] ^= nums[i]
                    nums[i] ^= nums[j]
        res = "".join([str(i) for i in nums])
        if int(res) == 0:
            return "0"
        return res


f = Solution()
nums = [10, 2]
print("nums: {}, f.largestNumber(nums): {}".format(nums, f.largestNumber(nums)))
nums = [3, 30, 34, 5, 9]
print("nums: {}, f.largestNumber(nums): {}".format(nums, f.largestNumber(nums)))
nums = [9, 6, 3, 0, 7, 4, 1, 8, 5, 2]
print("nums: {}, f.largestNumber(nums): {}".format(nums, f.largestNumber(nums)))
