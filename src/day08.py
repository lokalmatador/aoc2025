from utils.api import *
from scipy.spatial.distance import euclidean
import itertools

input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
# input_str = get_input(8)

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    boxes = [[int(c) for c in x.split(",")] for x in get_input(8).splitlines()]
    N = len(boxes)
    p = [i for i in range(N)]
    size = [1] * N
    order = [(euclidean(boxes[i], boxes[j]), i, j) for i in range(N) for j in range(i + 1, N)]
    order.sort(reverse=True)
    max_num = 1000

    for count in range(max_num):
        d, i, j = order.pop()
        union(p, size, i, j)

    size.sort(reverse=True)

    return size[0] * size[1] * size[2]


def part2() -> int:
    boxes = [[int(c) for c in x.split(",")] for x in get_input(8).splitlines()]
    N = len(boxes)
    p = [i for i in range(N)]
    size = [1] * N
    order = [(euclidean(boxes[i], boxes[j]), i, j) for i in range(N) for j in range(i + 1, N)]
    order.sort(reverse=True)

    while True:
        d, i, j = order.pop()
        union(p, size, i, j)

        if size[find(p, i)] == N:
            return boxes[i][0] * boxes[j][0]


def find(p, a):
    if a != p[a]:
        p[a] = find(p, p[a])

    return p[a]


def union(p, size, a, b):
    a, b = find(p, a), find(p, b)
    if a == b:
        return

    if size[a] > size[b]:
        a, b = b, a

    p[a] = b
    size[b] += size[a]
    size[a] = 0

