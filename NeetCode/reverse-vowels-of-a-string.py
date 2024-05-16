class Solution1:

    def reverseVowels(self, s: str) -> str:
        s_arr = [i for i in s]
        vowels = 'aeiou'
        i = 0
        j = len(s_arr) - 1
        while i <= j:
            if s_arr[i] in vowels and s_arr[j] in vowels:
                s_arr[i], s_arr[j] = s_arr[j], s_arr[i]
                i += 1
                j -= 1
            elif s_arr[i] in vowels and s_arr[j] not in vowels:
                j -= 1
            elif s_arr[i] not in vowels and s_arr[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(s_arr)


class Solution:
    def is_vowel(self, c):
        return c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u'

    def reverseVowels(self, s: str) -> str:
        s_arr = [i for i in s]
        vowels = 'aeiou'
        i = 0
        j = len(s) - 1
        while i < j:
            if self.is_vowel(s_arr[i]) and self.is_vowel(s_arr[j]):
                s_arr[i], s_arr[j] = s_arr[j], s_arr[i]
                i += 1
                j -= 1
            elif self.is_vowel(s_arr[i]) and not self.is_vowel(s_arr[j]):
                j -= 1
            elif not self.is_vowel(s_arr[i]) and self.is_vowel(s_arr[j]):
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(s_arr)


s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))
