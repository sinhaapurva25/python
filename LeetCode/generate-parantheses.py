class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=list()
        def helper(s: str, open_count: int, close_count: int):
            if len(s) == 2*n:
                res.append(s)
                return
            if open_count < n:
                helper(s+"(",open_count+1,close_count)
            if close_count < open_count:
                helper(s+")", open_count, close_count+1)
        helper("", 0, 0)
        return res

        