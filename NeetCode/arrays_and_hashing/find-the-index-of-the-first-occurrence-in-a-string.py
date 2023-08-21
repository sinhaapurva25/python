class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            wrd = haystack[i:i+len(needle)]
            if wrd == needle:
                return i
        return -1
s = Solution()
print(s.strStr(haystack = "sadbutsad", needle = "sad"))
print(s.strStr(haystack = "leetcode", needle = "leeto"))
