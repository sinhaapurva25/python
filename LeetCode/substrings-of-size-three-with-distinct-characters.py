from collections import Counter


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        freq = dict()
        for i in range(len(s)-2):
            if i == 0:
                freq = Counter(s[i:i+3])
            else:
                freq[s[i-1]] -= 1
                if freq[s[i-1]] == 0:
                    freq.pop(s[i - 1])
                freq[s[i+2]] = 1 + freq.get(s[i+2], 0)

            if len(freq) == 3:
                res += 1
        return res

s = Solution()
s.countGoodSubstrings(s = "xyzzaz")
s.countGoodSubstrings(s = "aababcabc")