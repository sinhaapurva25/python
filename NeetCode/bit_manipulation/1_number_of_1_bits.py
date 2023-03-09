# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         n = str(n)
#         res = 0
#         for i in n:
#             if i is '1':
#                 res +=1
#         return res
# f = Solution()
# print(f.hammingWeight(int(str(1011))))
# print(f.hammingWeight(int(str(10000000))))
# print(f.hammingWeight(int(str(11111111111111111111111111111101))))
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(n)
        res = 0
        for i in n:
            if i is '1':
                res +=1
        return res
        # return sum([int(x) for x in bin(n)[2:]])
f = Solution()
print(f.hammingWeight(1011))
print(f.hammingWeight(10000000))
print(f.hammingWeight(11111111111111111111111111111101))