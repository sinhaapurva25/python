class Solution:
    def isHappy(self, n: int) -> bool:
        all_sum = list()
        while True:
            digits = list()
            m = n
            while m!=0:
                digits.append(m%10)
                m //= 10
            s = 0
            for i in digits:
                s += i*i
            n = s
            # if n<=9 or s in all_sum:
            if n==1 or s in all_sum:
                break
            all_sum.append(s)
        if n == 1:
            return True
        else:
            return False

f = Solution()
print(f.isHappy(19))
print(f.isHappy(2))
print(f.isHappy(1111111))