import math


class Solution:
    def swap(self, arr, x, y):
        arr[x] ^= arr[y]
        arr[y] ^= arr[x]
        arr[x] ^= arr[y]

    def getBinSum(self, a, b) -> str:
        if len(a) > len(b):
            b = f"{'0' * (len(a) - len(b))}{b}"
            l = len(a)
        elif len(b) > len(a):
            a = f"{'0' * (len(b) - len(a))}{a}"
            l = len(b)
        else:
            l = len(a)
        res = [''] * l
        c = 0
        dct = {'000': 0,
               '001': 0,
               '010': 0,
               '011': 1,
               '100': 0,
               '101': 1,
               '110': 1,
               '111': 1}
        for i in range(l):
            s = int(a[l - i - 1]) ^ int(b[l - i - 1]) ^ c
            c_class = f'{a[l - i - 1]}{b[l - i - 1]}{str(c)}'
            c = dct[c_class]
            res[l - i - 1] = str(s)
        r = f"{str(c)}{''.join(res)}"
        return r

    def decimal_to_binary(self, n: float) -> str:
        num = n
        if n < 0:
            n *= -1
        n, f = list(map(int, str(n).split('.')))
        f = float(f'0.{str(f)}') if f != 0 else 1.0
        if n == 0:
            return '0'
        r = list()
        while n != 0:
            r.append(str(n % 2))
            n //= 2
        for i in range(len(r) // 2):
            r[i], r[len(r) - i - 1] = r[len(r) - i - 1], r[i]
        # r.append('.')
        # if f<1.0:
        #     while f!=0:
        #         f *= 2
        #         r.append(str(int(f)))
        #         f = list(map(int, str(b).split('.')))[0]
        # else:
        #     r.append('0')
        res = ''.join(r)
        if num < 0:
            r = ''.join(['1' if x == 0 else '0' for x in r])
            res = self.getBinSum(r, '1')
        return res

    def bin_to_dec(self, b) -> int:
        d = [0] * len(b)
        for i in range(len(b)):
            if b[i] == '1':
                d[i] = int(math.pow(2, len(b) - i - 1))
        return sum(d)

    def getSum(self, a: float, b: float):
        a = self.decimal_to_binary(float(a))
        b = self.decimal_to_binary(float(b))
        r = self.getBinSum(a, b)
        return self.bin_to_dec(r)


f = Solution()
# print(f.getSum(7, 8))
# print(f.getSum(7, 8.0))
# print(f.getSum(7.0, 8))
# print(f.getSum(7.0, 8.0))
# print(f.getSum(7, 9))
# print(f.getSum(7, 10))
#
# print(f.getSum(-1, 1))
# print(f.decimal_to_binary(float(73)))
print(f.decimal_to_binary(float(-47)))
# print(f.getBinSum('0101001', '1'))
# print(f.decimal_to_binary(float(2.625)))

# print(f.decimal_to_binary(float(2.44)))
# print(f.decimal_to_binary(float(2.0)))
# print(f.decimal_to_binary(float(2)))

# for i in range(20):
#     print(f.decimal_to_binary(i))
