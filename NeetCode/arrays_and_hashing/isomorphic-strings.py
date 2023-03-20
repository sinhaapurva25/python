class Solution:
    def get_count(self, s) -> list:
        if len(s) == 0:
            dct = []
        elif len(s) == 1:
            dct = [s + '1']
        else:
            dct = [s[0] + '1']
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    initial_count = int(dct[len(dct) - 1][1:])
                    dct[len(dct) - 1] = s[i] + str(initial_count + 1)
                else:
                    dct.append(s[i] + '1')
        return dct

    def isIsomorphic(self, s: str, t: str) -> bool:

        s_count = self.get_count(s)
        t_count = self.get_count(t)

        if len(s_count) == len(t_count):
            replace_dct = {}
            for i in range(len(s_count)):
                if s_count[i][1:] != t_count[i][1:]:
                    return False
                else:
                    replace_dct[s_count[i][0]] = t_count[i][0]

            replace_dct_inv = {}
            for k, v in replace_dct.items():
                replace_dct_inv[v] = k

            replace_dct_inv_inv = {}
            for k, v in replace_dct_inv.items():
                replace_dct_inv_inv[v] = k

            if replace_dct == replace_dct_inv_inv:
                wrd = ''
                for i in range(len(s)):
                    wrd += replace_dct[s[i]]
            else:
                return False

            if wrd == t:
                return True
            else:
                return False
        else:
            return False


f = Solution()
print(f.isIsomorphic("egg", "add"))
print(f.isIsomorphic("foo", "bar"))
print(f.isIsomorphic("paper", "title"))
print(f.isIsomorphic("paperpp", "titlehh"))
print(f.isIsomorphic("badc", "baba"))
print(f.isIsomorphic("egcd", "adfd"))
