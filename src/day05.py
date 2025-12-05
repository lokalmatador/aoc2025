from utils.api import *

input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
# input_str = get_input(5)

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    ranges, ids = get_input(5).split("\n\n")
    ids = [int(x) for x in ids.splitlines()]
    ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in ranges.splitlines()]

    res = 0
    for id in ids:
        for r in ranges:
            if r[0] <= id <= r[1]:
                res+=1
                break

    return res


def part2() -> int:
    ranges, _ = get_input(5).split("\n\n")
    ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in ranges.splitlines()]
    ranges.sort(key=lambda x: x[0])

    i = 0
    while i < len(ranges) - 1:
        j = i + 1
        while j < len(ranges):
            if ranges[j][0] <= ranges[i][1]:
                ranges[i] = (ranges[i][0], max(ranges[j][1], ranges[i][1]))
                del ranges[j]
            else: j+=1
        i+=1

    res =0
    for r in ranges:
       res+=len(range(r[0], r[1]+1))

    return res
