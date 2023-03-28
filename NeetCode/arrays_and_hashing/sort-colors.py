class Solution:

    def sortColors(self, nums: list) -> None:
        i = 0
        j = 0
        k = 0

        for _ in nums:
            if _ == 0:
                i += 1
            elif _ == 1:
                j += 1
            else:
                k += 1

        j += i
        k += j

        _ = 0
        while _ < i:
            nums[_] = 0
            _ += 1
        while _ < j:
            nums[_] = 1
            _ += 1
        while _ < k:
            nums[_] = 2
            _ += 1


f = Solution()
nums = [2, 0, 2, 1, 1, 0, 0, 2, 2, 2, 1]
f.sortColors(nums)
print(nums)
nums = [2, 0, 1]
f.sortColors(nums)
print(nums)
