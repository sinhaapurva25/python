import math

class Solution:
    def rev(self, m: int) -> int:
        r = 0
        while m != 0:
            r = r * 10 + m % 10
            m //= 10
        return r

    def reverse(self, x: int) -> int:

        if x < 0:
            m = x * -1
            if 0 <= math.log2(m) <= 31:
                r = self.rev(m) * -1
            else:
                r = 0
        else:
            m = x
            if 0 <= math.log2(m + 1) <= 31:
                r = self.rev(m)
            else:
                r = 0
        return r


f = Solution()
print(f.reverse(123))
print(f.reverse(-123))
print(f.reverse(120))
# 2^31 = 2147483648
print(f.reverse(-2147483648))  # -(2^31)
print(f.reverse(-2147483649))  # -(2^31+1)
print(f.reverse(2147483647))  # (2^31 -1)
print(f.reverse(2147483648))  # (2^31)
print(f.reverse(1534236469))
