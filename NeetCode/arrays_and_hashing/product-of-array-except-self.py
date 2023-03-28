class Solution:
    def productExceptSelf(self, nums: list) -> list:
        l = 1
        r = 1
        l_arr = [0] * len(nums)
        r_arr = [0] * len(nums)

        for i in range(len(nums)):
            l = l * nums[i - 1] if i > 0 else 1
            l_arr[i] = l

            r = r * nums[len(nums) - i] if i > 0 else 1
            r_arr[len(nums) - i - 1] = r

        res_arr = [0] * len(nums)
        for i in range(len(nums)):
            res_arr[i] = l_arr[i] * r_arr[i]

        return res_arr


f = Solution()
print(f.productExceptSelf(nums=[1, 2, 3, 4]))
print(f.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
