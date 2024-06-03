class Solution:
    def validPalindrome(self, s: str) -> bool:
        # print("***** start *****")
        l, r = s[:len(s) // 2], s[(len(s) // 2) + 1 if len(s) % 2 == 1 else (len(s) // 2):][::-1]
        # print(s, l, r)
        if l == r:
            return True
        # print(" 1st check completed ")
        for i in range(len(s)):
            s_dash = s[:i] + s[i+1:]
            l, r = s_dash[:len(s_dash) // 2], s_dash[(len(s_dash) // 2) + 1 if len(s_dash) % 2 == 1 else (len(s_dash) // 2):][::-1]
            # print(s_dash, l, r)
            if l == r:
                return True
        # print("***** end *****")
        return False


f = Solution()
print(f.validPalindrome("aba"))
print(f.validPalindrome("abca"))
print(f.validPalindrome("yxaaxy"))
print(f.validPalindrome("abc"))
print(f.validPalindrome("acbca"))
print(f.validPalindrome("deeee"))
