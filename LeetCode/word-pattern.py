# from collections import defaultdict
# class Solution:
#     def map_pattern(self, pattern: str) -> dict:
#         dct = defaultdict(list)
#         for i in range(len(pattern)):
#             dct[pattern[i]].append(i)

#         dct = {str(j): i for i, j in enumerate(dct.values())}
#         return dct

#     def map_s(self, s: str) -> dict:
#         dct = defaultdict(list)
#         s = s.split(' ')
#         for i in range(len(s)):
#             dct[s[i]].append(i)

#         dct = {str(j): i for i, j in enumerate(dct.values())}
#         return dct

#     def wordPattern(self, pattern: str, s: str) -> bool:
#         dct_p = self.map_pattern(pattern)
#         dct_s = self.map_s(s)
#         if len(dct_p) == len(dct_s):
#             if dct_p == dct_s:
#                 return True
#             return False
#         return False
from collections import defaultdict
class Solution:
    def map_text(self, text: str, t: str = 'p') -> dict:
        dct = defaultdict(list)
        if t == 's':
            text = text.split(' ')
        for i in range(len(text)):
            dct[text[i]].append(i)

        dct = {str(j): i for i, j in enumerate(dct.values())}
        return dct

    def wordPattern(self, pattern: str, s: str) -> bool:
        dct_p = self.map_text(pattern)
        dct_s = self.map_text(s, 's')
        if len(dct_p) == len(dct_s):
            if dct_p == dct_s:
                return True
            return False
        return False


f = Solution()
# f.wordPattern(pattern="abba", s="dog cat cat dog")
# f.wordPattern(pattern="abba", s="dog cat cat fish")
# f.wordPattern(pattern="aaaa", s="dog cat cat dog")
print(f.wordPattern(pattern="abba", s="dog cat cat dog"))
print(f.wordPattern(pattern="abba", s="dog cat cat fish"))
print(f.wordPattern(pattern="aaaa", s="dog cat cat dog"))

# dct = {'a': [0, 3],
#        'b': [1, 2]}
# print(dct)
# dct = {str(j): i for i, j in enumerate(dct.values())}
# print(dct)

'''
{'[0, 3]': 0, '[1, 2]': 1}
{'[0, 3]': 0, '[1, 2]': 1}
{'[0, 1, 2, 3]': 0}
'''
