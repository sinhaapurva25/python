class Solution:
    def missingNumber(self, nums: list) -> int:
        n = 0
        s = 0
        for i in nums:
            s += i
            n += 1
        missing_num = n*(n+1)//2 - s
        return missing_num
f = Solution()
print(f.missingNumber([3,0,1]))
print(f.missingNumber([0,1]))
print(f.missingNumber([9,6,4,2,3,5,7,0,1]))