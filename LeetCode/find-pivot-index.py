class Solution:
    def pivotIndex(self, nums: list) -> int:
        s_l = 0
        left_arr = [0] * len(nums)
        s_r = 0
        right_arr = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                left_arr[i] = 0
                right_arr[len(nums) - i - 1] = 0
            else:
                left_arr[i] = s_l + nums[i - 1]
                s_l += nums[i - 1]
                right_arr[len(nums) - i - 1] = s_r + nums[len(nums) - i]
                s_r += nums[len(nums) - i]

        for i in range(len(nums)):
            if left_arr[i] == right_arr[i]:
                return i
        return -1


f = Solution()
print(f.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))  # 3
print(f.pivotIndex(nums=[1, 2, 3]))  # -1
print(f.pivotIndex(nums=[2, 1, -1]))  # 0
