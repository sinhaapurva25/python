class Solution:
    def plusOne(self, digits: list) -> list:
        if len(digits) < 1:
            return digits
        num = 0
        for i in digits:
            num = num*10 + i
        num += 1
        digits = list()
        while num!=0:
            digits.append(num%10)
            num //= 10
        for i in range(len(digits)//2):
            digits[i] ^= digits[len(digits)-i-1]
            digits[len(digits) - i - 1] ^= digits[i]
            digits[i] ^= digits[len(digits) - i - 1]
        return digits
f = Solution()
print(f.plusOne([1,2,3]))
print(f.plusOne([4,3,2,1]))
print(f.plusOne([9]))