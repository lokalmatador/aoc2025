from utils.api import *
from shapely import Polygon, Point
from itertools import product



input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
# input_str = get_input(9)

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    points = [(int(x[0]), int(x[1])) for x in [x.split(",") for x in get_input(9).splitlines()]]

    res = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x1 = points[i]
            x2 = points[j]
            area = (abs(x2[0] - x1[0]) + 1) * (abs(x2[1] - x1[1]) + 1)
            if area > res: res = area

    return res


def part2() -> int:
    points = [tuple(int(i) for i in x.split(",") if i != "") for x in get_input(9).splitlines()]
    p = Polygon(points)

    res = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1 = points[i]
            x2 = points[j]
            min_x = min(x1[0], x2[0])
            min_y = min(x1[1], x2[1])
            max_x = max(x1[0], x2[0])
            max_y = max(x1[1], x2[1])
            curr_poly = Polygon(((min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)))

            if p.contains(curr_poly):
                area = (abs(x2[0] - x1[0]) + 1) * (abs(x2[1] - x1[1]) + 1)
                if area > res: res = area

    return res