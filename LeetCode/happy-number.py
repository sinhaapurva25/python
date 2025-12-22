class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0: return False
        res = False
        cycle = set()
        while (n != 1) and (n not in cycle):
            cycle.add(n)
            sq = 0
            nm = n
            while nm != 0:
                sq += (nm % 10) * (nm % 10)
                nm //= 10
            n = sq
        if n == 1: return True
        return res

f = Solution()
print(f.isHappy(19))
print(f.isHappy(7))
print(f.isHappy(1111111))
print(f.isHappy(0))