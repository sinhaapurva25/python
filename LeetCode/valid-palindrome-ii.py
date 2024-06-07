class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return self.method_name(i + 1, j, s) | self.method_name(i, j - 1, s)
            i += 1
            j -= 1
        return True

    def method_name(self, x, y, s):
        while x < y:
            if s[x] != s[y]:
                return False
            x += 1
            y -= 1
        return True

f = Solution()
print(f.validPalindrome("aba"))
print(f.validPalindrome("abca"))
print(f.validPalindrome("yxaaxy"))
print(f.validPalindrome("abc"))
print(f.validPalindrome("acbca"))
print(f.validPalindrome("deeee"))
print(f.validPalindrome("cxcaac"))

# https://www.youtube.com/watch?v=wX3-411uJH0
# https://github.com/nikoo28/java-solutions/blob/master/src/main/java/leetcode/easy/ValidPalindromeII.java

# More challenges
# 1216. Valid Palindrome III
# 2330. Valid Palindrome IV
