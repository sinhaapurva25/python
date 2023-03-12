class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])

f = Solution()
print(f.lengthOfLastWord(s = "Hello World"))
print(f.lengthOfLastWord("   fly me   to   the moon  "))
print(f.lengthOfLastWord("luffy is still joyboy"))