# class Solution:
#     def heapify(self, arr, N, i):
#         largest = i
#         l = 2 * i + 1
#         r = 2 * i + 2
#
#         if l < N and arr[largest] < arr[l]:
#             largest = l
#
#         if r < N and arr[largest] < arr[r]:
#             largest = r
#
#         if largest != i:
#             arr[largest] ^= arr[i]
#             arr[i] ^= arr[largest]
#             arr[largest] ^= arr[i]
#
#             self.heapify(arr, N, largest)
#
#     def heap_sort(self, arr):
#         N = len(arr)
#
#         for i in range(N//2-1, -1, -1):
#             self.heapify(arr, N, i)
#
#         for i in range(N-1, 0, -1):
#             if i != 0:
#                 arr[i] ^= arr[0]
#                 arr[0] ^= arr[i]
#                 arr[i] ^= arr[0]
#             self.heapify(arr, i, 0)
#
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#
#         s_arr = [0] * len(s)
#         t_arr = [0] * len(s)
#         for i in range(len(s)):
#             s_arr[i] = ord(s[i])
#             t_arr[i] = ord(t[i])
#
#         self.heap_sort(s_arr)
#         self.heap_sort(t_arr)
#
#         res = True
#         for i in range(len(s)):
#             if s_arr[i] != t_arr[i]:
#                 res = False
#                 break
#         return res
# Runtime: 1560 ms; Beats: 5.1%
# Memory: 15 MB; Beats: 22.3%

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         i = 0
#         while i < len(s):
#             for j in range(len(t)):
#                 if s[i] == t[j]:
#                     t = t[:j] + t[j+1:]
#                     break
#             i += 1
#
#         if len(t) == 0:
#             return True
#         else:
#             return False
# Runtime: 2249 ms; Beats: 5.1%
# Memory: 14.4 MB; Beats: 95.77%

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = 1

        res1 = 1
        for i in s:
            res1 *= ord(i)
            x ^= ord(i)
        res2 = 1
        for i in t:
            res2 *= ord(i)
            x ^= ord(i)
        '''
        doing only XOR will fail for cases like s="tt", t="ss"
        doing only MUL will fail for cases like s="nl", t="cs"
        hence use a combination of both
        '''
        if res1 == res2 and x == 1:
            return True
        else:
            return False
# Runtime: 917 ms; Beats: 5.1%
# Memory: 14.4 MB; Beats: 60.64%

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         dct_s1 = {}
#         for i in s:
#             if i in dct_s1:
#                 dct_s1[i] += 1
#             else:
#                 dct_s1[i] = 1
#
#         res = True
#         for i in t:
#             if i in dct_s1:
#                 dct_s1[i] -= 1
#             else:
#                 return False
#         for i in dct_s1.keys():
#             if dct_s1[i] > 0:
#                 return False
#         return True
# Runtime: 40 ms; Beats: 91.70%
# Memory: 14.4 MB; Beats: 95.77%

f = Solution()
print(f.isAnagram(s="anagram", t="nagaram"))
print(f.isAnagram(s="rat", t="car"))

