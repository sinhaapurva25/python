import math


class Solution:
    def reverseBits(self, n: int) -> int:

        inverse = str()
        for i in range(len(str(n))):
            inverse += '0' if str(n)[len(str(n)) - i - 1] == '1' else '1'
        inverse = inverse[::-1]
        twos_complement = str()
        c = 1
        for i in range(len(inverse)):
            s = int(str(inverse)[len(str(inverse)) - i - 1]) ^ c
            c = int(str(inverse)[len(str(inverse)) - i - 1]) * c
            twos_complement += str(s)
        twos_complement = int(twos_complement)

        d = 0
        for i in range(len(str(twos_complement))):
            d += int(str(twos_complement)[len(str(twos_complement))-i-1])*math.pow(2, i)
        return d


s = Solution()
print(s.reverseBits(10))
print(s.reverseBits(101))
print(s.reverseBits(110))
print(s.reverseBits(111))
print(s.reverseBits(101011100))
print(s.reverseBits(10100101000001111010011100))
print(s.reverseBits(11111111111111111111111111111101))