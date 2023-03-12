# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         x = 1
#         res1 = 1
#
#         for i in s:
#             res1 *= ord(i)
#             x ^= ord(i)
#         res2 = 1
#         for i in t:
#             res2 *= ord(i)
#             x ^= ord(i)
#
#         if res1 == res2 and x == 1:
#             return True
#         else:
#             return False
#
#
#     def find_anagram_in_dct(self, i, dct_keys):
#         for j in dct_keys:
#             if self.isAnagram(i, j):
#                 return True, j
#         return False, -1
#
#     def groupAnagrams(self, strs: list) -> list:
#         if len(strs) <= 1:
#             return [strs]
#
#         dct = dict()
#         for i in range(len(strs)):
#             b, j = self.find_anagram_in_dct(strs[i], dct.keys())
#             if b == True:
#                 dct[j].append(strs[i])
#             else:
#                 dct[strs[i]] = [strs[i]]
#
#         return [i for i in dct.values()]
# code fails at runtime of the above code
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        if len(strs) <= 1:
            return [strs]
        strs_sorted = [''.join(sorted(i)) for i in strs]

        dct = {}
        for i in range(len(strs_sorted)):
            if strs_sorted[i] in dct:
                dct[strs_sorted[i]].append(strs[i])
            else:
                dct[strs_sorted[i]] = [strs[i]]
        return [i for i in dct.values()]


f = Solution()
print(f.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(f.groupAnagrams(strs=[""]))
print(f.groupAnagrams(strs=["a"]))
print(f.groupAnagrams(
    strs=["eat", "tea", "tan", "ate", "nat", "bat", "ac", "bd", "aac", "bbd", "aacc", "bbdd", "acc", "bdd"]))
print(f.groupAnagrams(strs=["bbdd", "bdd", "aacc", "acc"]))
# print(f.isAnagram("bbdd", "bdd"))
# print(f.isAnagram("aacc", "acc"))
print(f.groupAnagrams(strs=["bbdd", "bdd"]))
