from collections import Counter


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        res = ''
        for i in range(len(s)+1):
            for j in range(i+1, len(s)+1):
                f = list(set([k for k in s[i:j]]))
                isNice = 1
                for c in f:
                    if (str(c).isupper() and str(c).lower() in f) or \
                            (str(c).islower() and str(c).upper() in f):
                        isNice *= 1
                    else:
                        isNice = 0
                        break
                if isNice == 1:
                    if len(s[i:j]) > len(res):
                        res = s[i:j]
        return res
                    
                
                

s = Solution()
print(s.longestNiceSubstring("YazaAay"))
print(s.longestNiceSubstring("Bb"))
print(s.longestNiceSubstring("c"))