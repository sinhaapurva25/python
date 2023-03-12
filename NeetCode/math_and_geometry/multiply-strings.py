class Solution:

    def string_to_number(self, num: str) -> int:
        l = len(num)

        n = 0
        i = 0
        m = num
        while i != len(m):
            d = m[len(m) - i - 1]
            n = n * 10 + ord(d) - 48
            num = num[:len(m) - i - 1]
            i += 1

        num = 0
        i = 0
        while n != 0:
            num = num * 10 + (n % 10)
            n //= 10
            i += 1
        if i < l:
            for i in range(l-i):
                num *= 10

        return num

    def string_to_numeric_arr(self, num: str) -> list:
        n = 0
        i = 0
        m = num
        while i != len(m):
            d = m[len(m) - i - 1]
            n = n * 10 + ord(d) - 48
            num = num[:len(m) - i - 1]
            i += 1
        m = [0] * len(m)
        i = 0
        while n != 0:
            m[i] = n % 10
            n //= 10
            i += 1
        return m

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        elif num1 == '1':
            return num2
        elif num2 == '1':
            return num1
        else:
            if len(num2) > len(num1):
                temp = num1
                num1 = num2
                num2 = temp

            num1 = self.string_to_number(num1)
            num2 = self.string_to_numeric_arr(num2)

            s = 0
            for i in range(len(num2)):
                m = 1
                for j in range(len(num2) - i - 1):
                    m *= 10
                s += num1 * num2[i] * m

            i = 0
            res = list()
            while s != 0:
                res.append(chr(s % 10 + 48))
                s //= 10
                i += 1

            return ''.join(res)[::-1]


f = Solution()
print(f.multiply(num1="2", num2="3"))
print(f.multiply(num1="123", num2="456"))
print(f.multiply(num1="3", num2="990"))
print(f.multiply(num1="3", num2="450"))
print(f.multiply(num1="3", num2="45000"))
print(f.multiply(num1="3", num2="90000"))
'''
num1 = "2", num2 = "3"
Output: "6"

Input: num1 = "123", num2 = "456"
Output: "56088"
'''
