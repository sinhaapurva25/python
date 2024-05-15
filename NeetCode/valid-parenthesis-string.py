class Solution:
    def checkValidString(self, s: str):
        lst = list()
        for i in s:
            if i == '(' or  i == ')':
                lst.append(i)
        return lst
f = Solution()
print(f.checkValidString('()'))


