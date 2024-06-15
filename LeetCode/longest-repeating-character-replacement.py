class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # BRUTE FORCE SOLUTION
        # mx = 0
        # for i in range(len(s)):
        #     tmp = list()
        #     for j in range(i, len(s)):
        #         tmp.append(s[j])
        #         sub = "".join(tmp)
        #
        #         freq = dict()
        #         for char in sub:
        #             if char in freq:
        #                 freq[char] += 1
        #             else:
        #                 freq[char] = 1
        #
        #         if len(sub) - max([v for v in freq.values()]) <= k:
        #             if len(sub) > mx:
        #                 mx = len(sub)
        # return mx

        # SLIDING WINDOW SOLUTION
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            print("substring: {}".format(s[l:r]))
            if r-l+1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

s = Solution()
print(s.characterReplacement(s="ABAB", k=2))
print(s.characterReplacement(s="AABABBA", k=1))
print(s.characterReplacement(s="AAAA", k=2))

# Next challenges:
# Longest Substring with At Most K Distinct Characters
# Max Consecutive Ones III
# Minimum Number of Operations to Make Array Continuous
# Maximize the Confusion of an Exam
# Longest Substring of One Repeating Character
