class Solution:
    def grayCode(self, n: int):
        f = 1
        for i in range(n):
            f *= 2
        
        res = list()
        for i in range(f):
            gray = i ^ (i >> 1)
            res.append(gray)
        return res
f = Solution()
f.grayCode(16)