class Solution:

    def checkIfNonAlphaChar(self, ch):
        if (not (ord('a') <= ord(ch) <= ord('z'))) and (not (ord('A') <= ord(ch) <= ord('Z'))):
            return True
        return False

    def reverseOnlyLetters(self, s: str) -> str:
        res = [i for i in s]
        i = 0
        j = len(s) - 1
        while i < j:
            if not(self.checkIfNonAlphaChar(s[i])) \
                    and \
                    not(self.checkIfNonAlphaChar(s[j])):
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
            if self.checkIfNonAlphaChar(s[i]):
                i += 1
            if self.checkIfNonAlphaChar(s[j]):
                j -= 1
        return ''.join(res)


s = Solution()
# print(s.reverseOnlyLetters("ab-cd"), s.reverseOnlyLetters("ab-cd") == "dc-ba")
# print(s.reverseOnlyLetters(s="a-bC-dEf-ghIj"), s.reverseOnlyLetters(s="a-bC-dEf-ghIj") == "j-Ih-gfE-dCba")
# print(s.reverseOnlyLetters(s="Test1ng-Leet=code-Q!") ,s.reverseOnlyLetters(s="Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!")
# print(s.reverseOnlyLetters(s=";1yDV"), s.reverseOnlyLetters(s=";1yDV") == ";1VDy")
print(s.reverseOnlyLetters(s="z<*zj"), s.reverseOnlyLetters(s="z<*zj") == "j<*zz")
# print(ord(';'))

# print(s.checkIfNonAlphaChar(";"))
print(s.checkIfNonAlphaChar("<"))
