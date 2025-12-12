import numpy as np

from utils.api import *

input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
input_str = get_input(7)

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    rows = input_str.splitlines()
    current = list(rows[0].replace("S", "|"))
    res = 0

    for row in rows[1:]:
        temp = list(current)

        for i in range(len(row)):
            if row[i] == '^' and temp[i] == "|":
                temp[i-1] = "|"
                temp[i+1] = "|"
                temp[i] = "."
                res += 1

        current = list(temp)

    return res


def part2() -> int:
    data = np.array([list(row) for row in input_str.splitlines()])
    manifold = np.zeros_like(data, dtype=np.int64)
    manifold[data == 'S'] = 1

    for i in range(1, len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '.':
                manifold[i][j] += manifold[i - 1][j]
        for j in range(len(data[0])):
            if data[i][j] == '^':
                manifold[i][j - 1] += manifold[i - 1][j]
                manifold[i][j + 1] += manifold[i - 1][j]

    return np.sum(manifold[-1])