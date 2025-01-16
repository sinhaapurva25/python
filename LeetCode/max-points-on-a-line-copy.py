# python3 program to find maximum number of 2D points that lie on the same line.

from collections import defaultdict
from math import gcd
from typing import DefaultDict, List, Tuple

IntPair = Tuple[int, int]


def normalized_slope(a: IntPair, b: IntPair) -> IntPair:
    """
    Returns normalized (rise, run) tuple. We won't return the actual rise/run
    result in order to avoid floating point math, which leads to faulty
    comparisons.

    See
    https://en.wikipedia.org/wiki/Floating-point_arithmetic#Accuracy_problems
    """
    run = b[0] - a[0]

    # normalize undefined slopes to (1, 0)
    if run == 0:
        return (1, 0)

    # normalize to left-to-right
    if run < 0:
        a, b = b, a
        run = b[0] - a[0]

    rise = b[1] - a[1]
    # Normalize by greatest common divisor.
    # math.gcd only works on positive numbers.
    gcd_ = gcd(abs(rise), run)
    return (
        rise // gcd_,
        run // gcd_,
    )


def maximum_points_on_same_line(points: List[List[int]]) -> int:
    # You need at least 3 points to potentially have non-collinear points.
    # For [0, 2] points, all points are on the same line.
    if len(points) < 3:
        return len(points)

    # Note that every line we find will have at least 2 points.
    # There will be at least one line because len(points) >= 3.
    # Therefore, it's safe to initialize to 0.
    max_val = 0

    for a_index in range(0, len(points) - 1):
        # All lines in this iteration go through point a.
        # Note that lines a-b and a-c cannot be parallel.
        # Therefore, if lines a-b and a-c have the same slope, they're the same
        # line.
        a = tuple(points[a_index])
        # Fresh lines already have a, so default=1
        slope_counts: DefaultDict[IntPair, int] = defaultdict(lambda: 1)

        for b_index in range(a_index + 1, len(points)):
            b = tuple(points[b_index])
            slope_counts[normalized_slope(a, b)] += 1

        max_val = max(
            max_val,
            max(slope_counts.values()),
        )

    return max_val


print(maximum_points_on_same_line([
    [-1, 1],
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 3],
    [3, 4],
]))

# This code is contributed by Jose Alvarado Torre
