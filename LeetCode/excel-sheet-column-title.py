class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = list()
        while columnNumber > 0:
            columnNumber -= 1
            mod = columnNumber % 26
            res.append(chr(mod+65))
            columnNumber //= 26
        return "".join(res[::-1])

        

s = Solution()
print(s.convertToTitle(8396))
print(s.convertToTitle(761))
print(s.convertToTitle(780))