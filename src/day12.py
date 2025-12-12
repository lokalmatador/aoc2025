from utils.api import *
import math

input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
input_str = get_input(12)

# WRITE YOUR SOLUTION HERE

def parse_input():
    blocks = input_str.split("\n\n")
    placements = [x.replace("x", " ").replace(":", "").split(" ") for x in blocks[-1].splitlines()]
    return [[int(y) for y in x] for x in placements]


def part1() -> int:
    amounts = parse_input()
    return sum(x * y >= sum(z) * 7 for x, y, *z in amounts) - 1


def part2() -> int:
    res = 0
    return res
