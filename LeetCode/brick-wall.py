from collections import defaultdict


class Solution:
    def leastBricks(self, wall: list) -> int:
        dct = defaultdict(int)

        for i in range(len(wall)):
            s = 0
            for j in range(len(wall[i])):
                s += wall[i][j]
                dct[s] += 1

        if len(dct) == 1:
            return len(wall)
        del dct[sum(wall[0])]
        return len(wall) - max(dct.values())


f = Solution()
print(f.leastBricks(wall=[[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]))
print(f.leastBricks(wall=[[1], [1], [1]]))
