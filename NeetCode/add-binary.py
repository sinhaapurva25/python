class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = 0
        c = 0
        a = int(a)
        b = int(b)
        while True:
            s = a ^ b
            c = a & b << 1
            if c == 0:
                break
            a = s
            b = c
        return s

f = Solution()
f.addBinary(a="11", b="1")
f.addBinary(a="1010", b="1011")

# Next challenges:
# Add to Array-Form of Integer
