class Solution:
    def missingRolls(self, rolls: list, mean: int, n: int) -> list:
        m = 0
        s1 = 0
        for i in rolls:
            m += 1
            s1 += i
        s2 = (mean * (m + n)) - s1

        res = list()
        if 0 < s2 <= n * 6 and s2 >= n:
            res = [s2 // n for i in range(n)]
            s = (s2 // n) * n
            i = 0
            while s != s2:
                res[i] += 1
                i += 1
                s += 1
                if i == n:
                    i = 0
        return res


f = Solution()
print(f.missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2))
print(f.missingRolls(rolls=[1, 5, 6], mean=3, n=4))
print(f.missingRolls(rolls=[1, 2, 3, 4], mean=6, n=4))
print(f.missingRolls(rolls=[6, 3, 4, 3, 5, 3], mean=1, n=6))
print(f.missingRolls(rolls=[4, 2, 2, 5, 4, 5, 4, 5, 3, 3, 6, 1, 2, 4, 2, 1, 6, 5, 4, 2, 3, 4, 2, 3, 3, 5, 4, 1, 4, 4, 5, 3, 6, 1, 5, 2,
           3, 3, 6, 1, 6, 4, 1, 3], mean=2, n=53))
