class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k == len(nums):
            return
        # while k > len(nums):
        #     k -= len(nums)
        # or you could do this:
        if k > len(nums):
            k = int(k % len(nums))

        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     res[(i + k) % len(nums)] = nums[i]
        # print(res)

        nums[:] = nums[-k:] + nums[:-k]



s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
s.rotate(nums, k=3)

nums = [-1, -100, 3, 99]
s.rotate(nums, k=3)

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s.rotate(nums, k=2)
