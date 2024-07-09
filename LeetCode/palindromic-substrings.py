class Solution:
    def countSubstrings(self, s: str) -> int:
        # res = 0
        # l = 0
        # r = l + 1
        # while l < r:
        #     if s[l:r] == s[l:r][::-1]:
        #         res += 1
        #     else:
        #         l += 1
        #     r += 1
        # return res
        res = 0
        for i in range(len(s)+1):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    res += 1
        return res

s = Solution()
print(s.countSubstrings("aaa"))
print(s.countSubstrings("abc"))