class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lst = list(s)
        for idx,i in enumerate(s_lst):
            if 65 <= ord(i) <= 90:
                s_lst[idx] = chr(ord(i) + 32)
            if not(i.isalnum()):
                s_lst[idx] = ""
        new_s = str("".join(s_lst))
        if new_s == new_s[::-1]:
            return True
        return False
        


f = Solution()
print(f.isPalindrome("A man, a plan, a canal: Panama"))
# print(f.isPalindrome("0P"))
# print(f.isPalindrome("a"))
# Next challenges:
# Palindrome Linked List
# Valid Palindrome II
# Maximum Product of the Length of Two Palindromic Subsequences
# Find First Palindromic String in the Array
# Valid Palindrome IV
# Maximum Palindromes After Operations
