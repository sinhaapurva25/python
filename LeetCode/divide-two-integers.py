
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # # BRUTE FORCE
        # left_range = -2147483648
        # right_range = 2147483647
        # if divisor == 0 or (dividend == left_range and divisor == -1):
        #     return right_range
        # if dividend == 0:
        #     return 0
        # dividend_abs = abs(dividend)
        # divisor_abs = abs(divisor)
        # if divisor_abs == 1:
        #     res = dividend_abs
        # else:
        #     res = 0
        #     while dividend_abs >= divisor_abs:
        #         dividend_abs -= divisor_abs
        #         res += 1
        # if (dividend < 0 and divisor < 0) or \
        #         dividend > 0 and divisor > 0:
        #     return min(res, right_range)
        # return max(-res, left_range)
        left_range = -2147483648
        right_range = 2147483647
        if divisor == 0 or (dividend == left_range and divisor == -1):
            return right_range
        if dividend == 0:
            return 0
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):  sign = 1
        else: sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            return dividend if (sign == 1) else -dividend
        import math
        ans = math.ceil(math.exp(math.log(dividend) - math.log(divisor)))
        return ans if (sign == 1) else -ans
s = Solution()
# print(s.divide(10, 3))
# print(s.divide(-7, 3))
# print(s.divide(-7, 3))
# print(s.divide(2147483647, 2))
# print(s.divide(-70, 2))
print(s.divide(-231, 3))

# # EDGE CASES
# print(s.divide(-2147483648, -1))
# print(s.divide(-2147483648, 0))
# print(s.divide(0, 0))
# print(s.divide(0, 2147483647))
# print(s.divide(2147483647, 0))
