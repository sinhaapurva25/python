# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         n = f'0b{str(n)}'
#         res = 0
#         for i in n:
#             if i is '1':
#                 res +=1
#         return res
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
f= Solution()
print(f.hammingWeight(1011))
print(f.hammingWeight(10000000))
print(f.hammingWeight(11111111111111111111111111111101))