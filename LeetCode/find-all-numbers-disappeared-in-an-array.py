from collections import defaultdict
class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        dct = {i: 1 for i in nums}
        dct = defaultdict(int, dct)
        res = []
        for i in range(1, len(nums) + 1):
            if dct[i] == 0:
                res.append(i)
        return res


f = Solution()
print(f.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(f.findDisappearedNumbers([1, 1]))
print(f.findDisappearedNumbers([1, 1, 2, 2]))
