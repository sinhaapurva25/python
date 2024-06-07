class Solution:
    def singleNumber(self, nums: list) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
f= Solution()
print(f.singleNumber([2,2,1]))
print(f.singleNumber([4,1,2,1,2]))
print(f.singleNumber([1]))