class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        i = 0
        while True:
            s = int(str(num)[i:i + k])
            if int(s) != 0 and num % int(s) == 0:
                res += 1
            i += 1
            if i > len(str(num)) - k:
                break
        return res


s = Solution()
print(s.divisorSubstrings(num=240, k=2))
print(s.divisorSubstrings(num=430043, k=2))
print(s.divisorSubstrings(num=2, k=1))
print(s.divisorSubstrings(num=30003, k=3))
