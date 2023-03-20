class Solution:
    def generate(self, numRows: int) -> list:
        res = list()

        for i in range(numRows):
            if i == 0:
                res.append([1])
            else:
                k = [0]+res[i - 1]
                l = res[i - 1]+[0]
                res.append([k[s]+l[s] for s in range(i+1)])
        return res


f = Solution()
print(f.generate(numRows=5))
print(f.generate(numRows=1))
