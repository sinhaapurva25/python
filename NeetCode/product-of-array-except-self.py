class Solution:
    def productExceptSelf(self, nums: list) -> list:
        l = 1
        r = 1
        left_nums = [0] * len(nums)
        right_nums = [0] * len(nums)
        prod_except_self = [0] * len(nums)
    
        for i in range(len(nums)):
            if i > 0:
                l *= nums[i - 1]
                r *= nums[len(nums) - i]
            left_nums[i] = l
            right_nums[len(nums) - i - 1] = r
    
        for i in range(len(nums)):
            prod_except_self[i] = left_nums[i] * right_nums[i]
        left_nums.clear()
        right_nums.clear()
        return prod_except_self
    
    def productExceptSelfSol1(self, nums: list) -> list:
        l = 1
        r = 1
        l_nums = [0] * len(nums)
        r_nums = [0] * len(nums)

        for i in range(len(nums)):
            l = l * nums[i - 1] if i > 0 else 1
            l_nums[i] = l

            r = r * nums[len(nums) - i] if i > 0 else 1
            r_nums[len(nums) - i - 1] = r

        res_nums = [0] * len(nums)
        for i in range(len(nums)):
            res_nums[i] = l_nums[i] * r_nums[i]

        return res_nums


f = Solution()
print(f.productExceptSelf(nums=[1, 2, 3, 4]))
print(f.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
