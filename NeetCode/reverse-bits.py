import math


class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(00000010100101000001111010011100, 'b')
        print(n)
        # res = 0
        # for i in range(len(str(n))):
        #     res += int(str(n)[i]) * int(math.pow(2, i))
        # return res


s = Solution()
# print(s.reverseBits(10))
# print(s.reverseBits(101))
# print(s.reverseBits(110))
# print(s.reverseBits(111))
# print(s.reverseBits(101011100))
# print(s.reverseBits(10100101000001111010011100))
print(s.reverseBits(00000010100101000001111010011100))
# print(s.reverseBits(10100101000001111010011100))
