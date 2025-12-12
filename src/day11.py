from functools import cache

from utils.api import *

input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
input_str = get_input(11)

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    devices = dict([(x[0], x[1].split(" ")) for x in [y.split(": ") for y in input_str.splitlines()]])

    @cache
    def dfs(node: str) -> int:
        if node == "out":
            return 1
        return sum(dfs(neighbor) for neighbor in devices[node])

    return dfs("you")


def part2() -> int:
    devices = dict([(x[0], x[1].split(" ")) for x in [y.split(": ") for y in input_str.splitlines()]])

    @cache
    def dfs(node: str, fft: bool, dac: bool) -> int:
        if node == "out":
            return 1 if (fft and dac) else 0
        return sum(dfs(neighbor, fft or neighbor == "fft", dac or neighbor == "dac") for neighbor in devices[node])

    return dfs("svr", False, False)


