import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        # return int(math.log2(243) / math.log2(3)) == math.log2(243) / math.log2(3)
        i = 0
        while True:
            p = math.pow(3, i)
            if p == n:
                return True
            if p > n:
                return False
            i += 1
s = Solution()
print(s.isPowerOfThree(27),
s.isPowerOfThree(0),
s.isPowerOfThree(-1),
s.isPowerOfThree(243))
