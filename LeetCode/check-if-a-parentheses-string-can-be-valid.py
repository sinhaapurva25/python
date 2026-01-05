class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:        
        allCombs = self.generateParentheses(len(s)//2)
        if s in allCombs:
            return True
        s_list = list(s)
        for i in range(len(s)):
            if locked[i] == '0':
                s_list[i] = '(' if s_list[i] == ')' else ')'
                if str(s_list) in allCombs:
                    return True
        return False

    def generateParentheses(self, n: int):
        res = list()
        def helper(s, open_count, close_count):
            if len(s) == 2*n:
                res.append(s)
                return
            if open_count < n:
                helper(s+'(', open_count+1, close_count)
            if close_count < n:
                helper(s+')', open_count, close_count+1)
        helper('', 0, 0)
        return res
f = Solution()
print(f.canBeValid(s = "))()))", locked = "010100"))