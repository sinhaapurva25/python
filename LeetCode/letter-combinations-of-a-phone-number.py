
class Solution:
    def letterCombinations(self, digits: str):
        
        keys = dict()
        x = 97
        for i in range(2, 10):
            t = 4 if (i == 7 or i == 9) else 3
            keys[i] = [chr(x+i) for i in range(t)]
            x += t

        if len(digits) == 1:
            res = keys[int(digits)]
        elif len(digits) == 2:
            res = list()
            for i in keys[int(digits[0])]:
                for j in keys[int(digits[1])]:
                    res.append(str(i)+str(j))
        elif len(digits) == 3:
            res = list()
            for i in keys[int(digits[0])]:
                for j in keys[int(digits[1])]:
                    for k in keys[int(digits[2])]:
                        res.append(str(i)+str(j)+str(k))
        else:
            res = list()
            for i in keys[int(digits[0])]:
                for j in keys[int(digits[1])]:
                    for k in keys[int(digits[2])]:
                        for l in keys[int(digits[3])]:
                            res.append(str(i)+str(j)+str(k)+str(l))
        return res

s = Solution()
print(s.letterCombinations('2'))
print(s.letterCombinations('23'))
# print(s.letterCombinations('234'))
# print(s.letterCombinations('2345'))
