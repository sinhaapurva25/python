class Solution:
    def swap(self, nums, x, y):
        if x != y:
            nums[x] ^= nums[y]
            nums[y] ^= nums[x]
            nums[x] ^= nums[y]

    def sortColors(self, nums: list) -> None:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == 1:
                if nums[j] == 0:
                    self.swap(nums, i, j)
                j -= 1
            else:
                i += 1

f = Solution()
nums = [0, 1, 0, 1, 1, 1]
f.sortColors(nums)
print(nums)