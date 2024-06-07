class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num!=0:
            if num%2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1
        return count

s = Solution()
print(s.numberOfSteps(num=14))
print(s.numberOfSteps(num=8))
print(s.numberOfSteps(num=123))

# Next challenges:
# Minimum Moves to Reach Target Score
# Count Operations to Obtain Zero