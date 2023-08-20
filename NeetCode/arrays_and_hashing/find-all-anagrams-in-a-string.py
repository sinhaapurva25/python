class Solution:
    def isAnagram(self, s1: list, s2: list):
        if len(s1)!=len(s2) or set(s1)!=set(s2):
            return False
        else:
            for i in range(len(s1)):
                if s1[i] in s2:
                    idx = s2.index(s1[i])
                    s2[idx] = ''
            if set(s2) == {''}:
                return True
            else:
                return False


    def findAnagrams(self, s: str, p: str):
        arr = list()
        for i in range(len(s)):
            if i + len(p) > len(s):
                pass
            else:
                a = s[i: i + len(p)]
                arr.append(a)

        res = list()
        for i in range(len(arr)):
            # if set(arr[i]) == set(list(p)):
            if self.isAnagram(list(arr[i]), list(p)):
                res.append(i)
        return res
    # def findAnagrams(self, s: str, p: str):
    #
    #     frequency_of_p = dict()
    #     for i in p:
    #         if i in frequency_of_p:
    #             frequency_of_p[i] += 1
    #         else:
    #             frequency_of_p[i] = 1
    #
    #     res = list()
    #
    #     for i in range(len(s)):
    #         if i + len(p) > len(s):
    #             pass
    #         else:
    #             a = s[i: i + len(p)]
    #
    #             frequency=dict()
    #             for j in a:
    #                 if j in frequency:
    #                     frequency[j] += 1
    #                 else:
    #                     frequency[j] = 1
    #             if frequency == frequency_of_p:
    #                 res.append(i)
    #
    #     return res


s = Solution()
res = s.findAnagrams('abab', 'ab')
print(res)
res = s.findAnagrams(s="cbaebabacd", p="abc")
print(res)

