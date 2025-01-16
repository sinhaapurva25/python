class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0
        while l <= r:
            mid = (l+r)//2
            if mid*mid > x:
                r = mid - 1
            elif mid*mid < x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res
s = Solution()
print(s.mySqrt(8))
print(s.mySqrt(25))
