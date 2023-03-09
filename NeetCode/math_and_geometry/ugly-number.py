# import math
# class Solution:
#     def isUgly(self, n: int) -> bool:
#         f = [2, 3, 5]
#         pf = list()
#         for i in range(1, int(math.sqrt(n))+1):
#             if n%i == 0:
#                 if i!=1:
#                     pf.append(i)
#                     pf.append(n//i)
#         res = True
#         for i in pf:
#             if i not in f:
#                 res = False
#                 break
#         return res


import math
class Solution:
    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        else:
            return True
    def isUgly(self, n: int) -> bool:
        # if the number of 0 or negative, return False
        if n <= 0:
            return False
        f = [2, 3, 5]
        pf = list()
        while n%2 == 0:
            pf.append(2)
            n /= 2
        for i in range(3, int(math.sqrt(n))+1, 2):
            while n%i == 0:
                pf.append(i)
                n //= i
        if n > 2:
            pf.append(int(n))
        res = True
        for i in pf:
            if i not in f:
                res = False
                break
        return res
f = Solution()
# print(f.isUgly(6))
# print(f.isUgly(1))
# print(f.isUgly(14))
# print(f.isUgly(8))
print(f.isUgly(0))