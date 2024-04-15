class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            n &= n - 1
            res += 1
        return res


s = Solution()
print(s.hammingWeight(0b00000000000000000000000000001011))
print(s.hammingWeight(0b00000000000000000000000010000000))
print(s.hammingWeight(0b11111111111111111111111111111101))

