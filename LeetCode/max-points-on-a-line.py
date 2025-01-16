from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]):
        if len(points) < 3:
            return len(points)
        res = list()
        for i in range(len(points)-1):
            lines = dict()
            pt1 = points[i]
            for j in range(i + 1, len(points)):
                pt2 = points[j]
                if pt1[0] == pt2[0]:
                    slope = float("-inf")
                else:
                    slope = (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])
                lines[slope] = 1 + lines.get(slope, 0)
            res.append(max(lines.values()))
        return max(res)+1


s = Solution()
print(s.maxPoints(points=[[1, 1], [2, 2], [3, 3]]))
print(s.maxPoints(points=[[1, 8], [2, 3], [3, 3]]))
print(s.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
print(s.maxPoints(points=[[3, 3], [1, 4], [1, 1], [2, 1], [2, 2]]))
print(s.maxPoints(points=[[0, 0], [4, 5], [7, 8], [8, 9], [5, 6], [3, 4], [1, 1]]))
