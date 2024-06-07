import math


class Solution:
    def reverseBits(self, n: int) -> int:
        print(format(n, '032b'))
        print(format(n, '032b')[::-1])
        return int(format(n, '032b')[::-1], 2)
print("len(00000010100101000001111010011100): ", len("00000010100101000001111010011100"))



s = Solution()
# print(10, s.reverseBits(10))
print(101, s.reverseBits(101))
# print(110, s.reverseBits(110))
# print(111, s.reverseBits(111))
# print(101011100, s.reverseBits(101011100))
# print(10100101000001111010011100, s.reverseBits(10100101000001111010011100))
# print(11111111111111111111111111111101, s.reverseBits(11111111111111111111111111111101))
