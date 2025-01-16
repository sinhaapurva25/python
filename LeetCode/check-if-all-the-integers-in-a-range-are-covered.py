from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = list()
        for i in ranges:
            arr.extend(i)
        arr.sort()
        for i in range(left, right + 1):
            if i not in arr:
                return False
        return True


s = Solution()
# print(s.isCovered(ranges=[[1, 2], [3, 4], [5, 6]], left=2, right=5))
# print(s.isCovered(ranges=[[1, 10], [10, 20]], left=21, right=21))
print(s.isCovered([[25, 42], [7, 14], [2, 32], [25, 28], [39, 49], [1, 50], [29, 45], [18, 47]], left=15, right=38))
