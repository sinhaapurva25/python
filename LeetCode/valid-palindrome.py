class Solution:
    def isPalindrome(self, s: str) -> bool:

        print(s, "".join([i for i in s.lower() if not i.isalnum()]))
        s_formatted = "".join([i for i in s.lower() if i.isalnum()]).replace(" ", "")
        # if len(s_formatted) == 1:
        #     if len(s) == 1: return True
        #     return False

        for i in range(len(s_formatted) // 2):
            if not s_formatted[i] == s_formatted[len(s_formatted) - i - 1]:
                return False
        return True


f = Solution()
print(f.isPalindrome("A man, a plan, a canal: Panama"))
print(f.isPalindrome("0P"))
print(f.isPalindrome("a"))
# Next challenges:
# Palindrome Linked List
# Valid Palindrome II
# Maximum Product of the Length of Two Palindromic Subsequences
# Find First Palindromic String in the Array
# Valid Palindrome IV
# Maximum Palindromes After Operations
