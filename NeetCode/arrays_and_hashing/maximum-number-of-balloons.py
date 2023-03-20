class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        dct = {s: 0 for s in 'balloon'}
        for i in text:
            if i == 'b' or i == 'a' or i == 'l' or i == 'o' or i == 'n':
                dct[i] += 1

        dct['l'] //= 2
        dct['o'] //= 2

        c = float('inf')
        for v in dct.values():
            if v < c:
                c = v

        return c


f = Solution()
print(f.maxNumberOfBalloons("nlaebolko"))
print(f.maxNumberOfBalloons("loonbalxballpoon"))
print(f.maxNumberOfBalloons("leetcode"))
print(f.maxNumberOfBalloons("balllllllllllloooooooooon"))
