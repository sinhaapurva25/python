class Solution:
    def decimal_to_binary(self,b:int) -> str:
        if b == 0:
            return '0'
        r = list()
        while b!=0:
            r.append(str(b%2))
            b //= 2
        for i in range(len(r)//2):
            r[i],r[len(r) - i - 1] = r[len(r) - i - 1],r[i]
        return ''.join(r)
    def countBits(self, n: int) -> list:
        res=[0]*(n+1)
        for i in range(n+1):
            b = list(str(self.decimal_to_binary(i)))
            s = sum(list(map(int,b)))
            res[i] = s
        return res

f = Solution()
print(f.countBits(2))
print(f.countBits(5))

