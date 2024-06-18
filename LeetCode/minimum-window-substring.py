class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # # BRUTE FORCE
        res = ''
        mn_len = float("inf")
        frq_t = self.getFreq(t, t)

        for i in range(len(s) - len(t) + 1):
            if s[i] in t:
                # print("i: {}; j:".format(i), end=" ")
                for j in range(i + len(t), len(s) + 1):
                    if j - i >= mn_len:
                        break
                    # # Range of j for which the substring can be found
                    # print(j, end=" ")
                    if j - i < mn_len:
                        frq_s = self.getFreq(s[i:j], t)
                        if self.t_exists_in_s(frq_s, frq_t):
                            # print("frq_t= {}, frq_s= {}, l={}, s={}, len(s[i:j])={}, j-i+1={}".format(frq_t, frq_s, j - i, s[i:j], len(s[i:j]), j-i), end=" ")
                            mn_len = j - i
                            res = s[i:j]
        return res

    def t_exists_in_s(self, frq_s, frq_t):
        if len(frq_s.keys()) < len(frq_t.keys()):
            return False
        for k in frq_t.keys():
            if k not in frq_s.keys():
                return False
            else:
                if frq_s[k] < frq_t[k]:
                    return False
        return True

    def getFreq(self, s, t):
        frq = {}
        for i in range(len(s)):
            if s[i] in t:
                frq[s[i]] = 1 + frq.get(s[i], 0)
        return frq


s = Solution()
print("res: ", s.minWindow(s="ADOBECODEBANC", t="ABC"))
print("res: ", s.minWindow(s="A___B___C___A__B__C__A_B_C_ABC", t="ABC"))
print("res: ", s.minWindow(s="a", t="a"))
print("res: ", s.minWindow(s="a", t="aa"))
print("res: ", s.minWindow(s="a", t="aa"))
print("res: ", s.minWindow(s="bba", t="ab"))
