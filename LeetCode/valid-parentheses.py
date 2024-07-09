class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {")": "(",
                       "]": "[",
                       "}": "{"}
        res = list()
        for i in s:
            if i in parantheses.values():
                res.append(i)
            else:
                if len(res) == 0 or (len(res) > 0 and res.pop() != parantheses[i]):
                    return False

        if len(res) > 0:
            return False
        return True


s = Solution()
print(s.isValid(s="()"))
print(s.isValid(s="()[]{}"))
print(s.isValid(s="(]"))
print(s.isValid(s="({)[]}"))
