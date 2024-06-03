class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            prefix = (len(a) - len(b)) * "0"
            b = prefix + b
        elif len(b) > len(a):
            prefix = (len(b) - len(a)) * "0"
            a = prefix + a
        s = 0
        c = 0

        sm = [""]*len(a)
        for i in range(len(a)-1, -1, -1):
            x = (int(a[i]), int(b[i]), c)
            if x in [(0, 0, 0),
                     (0, 1, 1),
                     (1, 0, 1),
                     (1, 1, 0)]:
                s = 0
            else:
                s = 1
            sm[i] = str(s)
            if x in [(0, 0, 0),
                     (0, 0, 1),
                     (0, 1, 0),
                     (1, 0, 0)]:
                c = 0
            else:
                c = 1
        res = str(c)+"".join(sm)
        return str(int(res))

f = Solution()
f.addBinary(a="11", b="1")
f.addBinary(a="1010", b="1011")

# Next challenges:
# Add to Array-Form of Integer
