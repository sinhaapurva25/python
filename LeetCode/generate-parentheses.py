# SEARCH FOR THIS ON CHATGPT:
# all possible words of length n from 2 distinct characters such that each character is used equal number of times without using itertools
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        n *= 2
        half_n = n // 2

        def backtrack(A_count, B_count, current):
            if len(current) == n:
                result.append(current)
                return
            if A_count < half_n:
                backtrack(A_count + 1, B_count, current + '(')
            if B_count < half_n:
                backtrack(A_count, B_count + 1, current + ')')

        backtrack(0, 0, '')
        return result


s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
