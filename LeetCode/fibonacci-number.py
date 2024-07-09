class Solution:
    def fib(self, n: int) -> int:
        a = -1
        b = 1
        i = 0
        while 1:
            c = a + b
            i += 1
            if i > n:
                break
            a = b
            b = c
        return c
s = Solution()
for i in range(10):
    print(s.fib(i))