class Solution:
    def dec_to_bin(self, n: int) -> int:
        if n == 0:
            return 0
        res = str()
        while n != 0:
            res += str(n % 2)
            n = n // 2
        return int(res[::-1])

    def dec_to_bin_count(self, n: int) -> int:
        if n == 0:
            return 0
        res = 0
        while n != 0:
            res += n % 2
            n = n // 2
        return res

    def countBits(self, n: int):
        res = list()
        for i in range(n+1):
            res.append(self.dec_to_bin_count(int(i)))
        return res


s = Solution()
print(s.countBits(11))
print(s.countBits(5))
# print(s.dec_to_bin(0))