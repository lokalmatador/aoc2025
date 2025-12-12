from utils.api import *

input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
input_str = get_input(4)

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    grid = dict()
    for i, l in enumerate(input_str.splitlines()):
        for j, e in enumerate(l):
            grid[(i, j)] = e

    res = dict()
    for key, value in grid.items():
        if value == "@" and reachable(key, grid): res[key] = value

    return len(res)


def part2() -> int:
    res = 0
    removed = True
    grid = dict()

    for i, l in enumerate(input_str.splitlines()):
        for j, e in enumerate(l):
            grid[(i, j)] = e

    while removed:
        cand = dict()
        removed = False

        for key, value in grid.items():
            if value == "@" and reachable(key, grid): cand[key] = value

        for key in cand.keys():
            removed = True
            grid[key] = "."

        res+=len(cand)

    return res


def reachable(idx, grid):
    res = 0

    for x in [(-1, -1), (1, -1), (-1, 1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        key = (idx[0] + x[0], idx[1] + x[1])
        if key in grid and grid[key] == "@": res += 1

    return res < 4