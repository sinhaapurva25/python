class Solution:
    def func(self, c, i, c_max, arr, s, numRows):
        while i < len(s):
            for j in range(numRows):
                if i < len(s):
                    arr[j][c] = s[i]
                    i += 1
            c += 1
            for j in range(numRows - 2, 0, -1):
                if i < len(s):
                    arr[j][c] = s[i]
                    i += 1
                    c += 1

            if i < len(s):
                new_2D_arr = [['' for j in range(c_max)] for i in range(numRows)]
                for k in range(numRows):
                    arr[k].extend(new_2D_arr[k])
                new_2D_arr.clear()

        res = list()
        for i in arr:
            for j in i:
                if j != '':
                    res.append(j)
        arr.clear()
        return ''.join(res)

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        c = 0
        i = 0
        c_max = numRows - 1
        arr = [['' for j in range(c_max)] for i in range(numRows)]
        res = self.func(c, i, c_max, arr, s, numRows)
        return res


f = Solution()
print(f.convert(s="PAYPALISHIRING", numRows=3))
print(f.convert(s="ABCDEFGHIJKLMN", numRows=3))
print(f.convert(s="ABCDEFGHIJKLM", numRows=3))
print(f.convert(s="ABCDEFGHIJKL", numRows=3))
print(f.convert(s="ABCDEFGHIJ", numRows=3))
print(f.convert(s="ABCDEFGHI", numRows=3))
print(f.convert(s="PAYPALISHIRING", numRows=4))
print(f.convert(s="A", numRows=1))