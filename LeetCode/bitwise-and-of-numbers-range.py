import math

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        # The below logic will double the input in case both are equal, hence add theed the above logic
        left_bin = str('{:032b}'.format(left))
        right_bin = str('{:032b}'.format(right))
        res = list()
        for idx in range(32):
            i = left_bin[idx]
            j = right_bin[idx]
            if i != j:
                break
            else:
                res.append(i)
        while idx < 32:
            res.append('0')
            idx += 1
        return int(''.join(res), 2)

s = Solution()
print(s.rangeBitwiseAnd(5, 7))
print(s.rangeBitwiseAnd(0, 0))
# print(int(math.pow(2, 31)-1))
print(s.rangeBitwiseAnd(1, int(math.pow(2, 31)-1)))

# # doubles up if edge case scenario is not added
print(s.rangeBitwiseAnd(1, 1))
print(s.rangeBitwiseAnd(2, 2))
print(s.rangeBitwiseAnd(33, 33))

