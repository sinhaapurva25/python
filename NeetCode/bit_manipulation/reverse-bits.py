import math


class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(n)
        s = 0
        for i in range(len(n)):
            s += int(i)*math.pow(2, len(n)-i-1)
        return s
f = Solution()
print(f.reverseBits(10100101000001111010011100))