from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = list()
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval
        merged.append(prev)
        return merged


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
