class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "" or len(t) > len(s):
            return ""

        # # BRUTE FORCE
        res = ""
        mn_len = float("inf")
        frq_t = dict()
        for i in range(len(t)):
            frq_t[t[i]] = 1 + frq_t.get(t[i], 0)

        i = len(s) - len(t)
        while i > -1:
            if s[i] in t:
                j = i + len(t)
                frq_s, match = self.getFreq(s[i:j], t, frq_t)
                print("i: {}, j:".format(i), end=" ")
                while j < len(s) + 1 and j - i < mn_len:
                    # j - i < mn_len is the same as mn_len > len(t)
                    # print("{} ".format(j), end=" ")
                    if self.t_exists_in_s(frq_s, frq_t):
                    # if frq_s.keys() == frq_t.keys():
                        mn_len = j - i
                        res = s[i:j]
                        print("i: {}, j: {}, frq_s: {}, frq_t: {}, res: {}, match: {}".format(i, j, frq_s, frq_t, res, match))
                    if j >= len(s):
                        break
                    if s[j] in t:
                        if (s[j] not in frq_s) or \
                                ((s[j] in frq_s) and (frq_s[s[j]] < frq_t[s[j]])):
                            frq_s[s[j]] = 1 + frq_s.get(s[j], 0)
                            if frq_s[s[j]] < frq_t[s[j]]:
                                match[s[j]] = True
                    j += 1
            # print("i: {} over".format(i))
            i -= 1
        return res

    def t_exists_in_s(self, frq_s, frq_t):
        if len(frq_s.keys()) != len(frq_t.keys()):
            return False
        for k in frq_t.keys():
            if frq_s[k] < frq_t[k]:
                return False
        return True

    def getFreq(self, s, t, frq_t):
        match = dict()
        frq = {}
        for i in range(len(t)):
            if s[i] in t:
                frq[s[i]] = 1 + frq.get(s[i], 0)
            if frq[s[i]] >= frq_t[s[i]]:
                match[s[i]] = True
        return frq, match

s = Solution()
# print("res: ", s.minWindow(s="ADOBECODEBANC", t="ABC"))
# print("res: ", s.minWindow(s="A___B___C___A__B__C__A_B_C_ABC", t="ABC"))
# print("res: ", s.minWindow(s="CBA_C_B_A__C__B__A___C___B___A", t="ABC"))
# print("res: ", s.minWindow(s="a", t="a"))
# print("res: ", s.minWindow(s="a", t="aa"))
# print("res: ", s.minWindow(s="a", t="aa"))
# print("res: ", s.minWindow(s="bba", t="ab"))
print("res: ", s.minWindow(s="aaaaaaaaaaaabbbbbcdd", t="abcdd"))
# frq_s={'a': 1, 'b': 4, 'c': 1, 'd': 2}
# frq_t={'c': 1, 'd': 2, 'a': 1, 'b': 1}
# match = None

