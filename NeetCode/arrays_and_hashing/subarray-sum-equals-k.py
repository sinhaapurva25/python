
class Solution:
    def subarraySum(self, nums: list, k: int) -> int:
        res = 0
        s = 0
        i = 0
        while i < len(nums):
            s += nums[i]
            if s >= k:
                if s == k:
                    res += 1
                s = 0
            i += 1
        return res


# class Solution:
#     def subarraySum(self, nums: list, k: int) -> int:
#         ans, n = 0, len(nums)
#         preSum = [nums[0]]
#         dic = {}
#         dic[0] = 1
#         for i in nums[1:]:
#             preSum.append(i+preSum[-1])
#         for i in preSum:
#             if i-k in dic:
#                 ans+=dic[i-k]
#             dic[i] = dic.get(i,0) + 1
#         return ans

f = Solution()
print(f.subarraySum(nums=[1, 1, 1], k=2))
print(f.subarraySum(nums=[1, 2, 3], k=3))
print(f.subarraySum(nums=[0, -1, 5, 4, 1, 3], k=4))
print(f.subarraySum(nums=[0, -1, 5, 4, -6, 10, 1, 3], k=4))
