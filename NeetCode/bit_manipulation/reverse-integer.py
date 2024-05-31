import math
class Solution:
    def reverse(self, x: int) -> int:

        n = str(x).split("-")
        if len(n) == 2:
            f = -1
            m = int(n[1])
        else:
            f = 1
            m = int(n[0])

        r = 0
        while m != 0:
            r = r * 10 + m % 10
            m //= 10
        r *= f

        n = str(r).split("-")
        if len(n) == 2:
            n = int(n[1])
            if math.log2(int(n)) > float(31):
                return 0
        else:
            if math.log2(int(n[0]) + 1) > float(31):
                return 0
        return r




f = Solution()
print(f.reverse(2147483648*2))
print(f.reverse(123))
print(f.reverse(-123))
print(f.reverse(120))
# 2^31 = 2147483648
print(f.reverse(-2147483648))  # -(2^31)
print(f.reverse(-2147483649))  # -(2^31+1)
print(f.reverse(2147483647))  # (2^31 -1)
print(f.reverse(2147483648))  # (2^31)
print(f.reverse(1534236469))
print(f.reverse(-2147483412))
print(f.reverse(1534236469))

# Next challenges:
# String to Integer (atoi)
# Reverse Bits
# A Number After a Double Reversal
# Count Number of Distinct Integers After Reverse Operations
