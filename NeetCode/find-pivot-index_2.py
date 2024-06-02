class Solution:
    def pivotIndex(self, nums: list) -> int:
        s_l = 0
        for i in nums:
            s_l += i

        s_r = 0
        for i in range(len(nums)):
            s_l -= nums[i]
            if i > 0:
                s_r += nums[i-1]
            if s_l == s_r:
                return i
        return -1


f = Solution()
print(f.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))  # 3
print(f.pivotIndex(nums=[1, 2, 3]))  # -1
print(f.pivotIndex(nums=[2, 1, -1]))  # 0

