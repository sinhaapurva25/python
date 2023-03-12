from itertools import combinations

class DetectSquares:

    def __init__(self):
        self.pts = list()

    def add(self, point: list) -> None:
        self.pts.append(point[0])

    def distSq(self, p, q):
        return (p[0] - q[0]) * (p[0] - q[0]) + \
            (p[1] - q[1]) * (p[1] - q[1])

    def is_square(self, i):
        p1, p2, p3, p4 = i
        d2 = self.distSq(p1, p2)  # from p1 to p2
        d3 = self.distSq(p1, p3)  # from p1 to p3
        d4 = self.distSq(p1, p4)  # from p1 to p4

        if d2 == 0 or d3 == 0 or d4 == 0:
            return False

        # If lengths if (p1, p2) and (p1, p3) are same, then
        # following conditions must be met to form a square.
        # 1) Square of length of (p1, p4) is same as twice
        # the square of (p1, p2)
        # 2) Square of length of (p2, p3) is same
        # as twice the square of (p2, p4)

        if d2 == d3 and 2 * d2 == d4 and \
                2 * self.distSq(p2, p4) == self.distSq(p2, p3):
            return True

        # The below two cases are similar to above case
        if d3 == d4 and 2 * d3 == d2 and \
                2 * self.distSq(p3, p2) == self.distSq(p3, p4):
            return True

        if d2 == d4 and 2 * d2 == d3 and \
                2 * self.distSq(p2, p3) == self.distSq(p2, p4):
            return True

        return False

    def count(self, point: list) -> int:
        if len(self.pts) <= 2:
            return None
        else:
            comb = [list(i)+point for i in list(list(combinations(self.pts, 3)))]
            res = 0
            for i in comb:
                if self.is_square(i):
                    res += 1
            return res

# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
obj.add([[3, 10]])
obj.add([[11, 2]])
obj.add([[3, 2]])
obj.add([[13, 22]])
obj.add([[3, 25]])
param_1 = obj.count([[11, 10]])
print(param_1)
param_2 = obj.count([[14, 8]])
print(param_2)
obj.add([[3, 2]])
obj.add([[11, 2]])
param_3 = obj.count([[11, 2]])
print(param_3)


'''
[3, 10], [11, 2], [3, 2], [11, 10], [14, 8], [11, 2], [11, 10]
'''