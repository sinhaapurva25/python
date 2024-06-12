import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        regex_pattern = re.compile(r"\^"+re.escape(p)+r"\^$")
        regex_pattern = re.compile(re.escape(p))
        match = regex_pattern.search(s)
        if match:
            print(match.group())
            return True
        return False


s = Solution()
print(s.isMatch(s="aa", p=r"a"))
print(s.isMatch(s="aa", p=r"*"))
print(s.isMatch(s="cb", p=r"?a"))
