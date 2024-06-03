class Solution:

    def getSum(self, a: int, b: int) -> int:
        while True:
            s = a^b
            c = (a&b) << 1
            if c == 0:
                break
            a = s
            b = c
        return s

f = Solution()
print(f.getSum(9, 11))
# print(f.getSum(7, 9))
# print(f.getSum(7, 10))
# print(f.getSum(-1, 1))

# for i in range(20):
#     if i % 2 == 0:
#         print(f.getSum(-i*-i*-1, i))
#     else:
#         print(f.getSum(-i, i*i))
