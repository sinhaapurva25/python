import sys
class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        sys.set_int_max_str_digits(100000)
        l = list(str(fact))
        res = 0
        for i in range(len(l)-1, -1, -1):
            if l[i] == '0':
                res += 1
            else:
                break
        return res
s = Solution()
s.trailingZeroes(5)
s.trailingZeroes(0)
s.trailingZeroes(13)