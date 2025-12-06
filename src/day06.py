import operator

from utils.api import *
import re
import numpy as np
import functools

input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
# input_str = get_input(6)

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    def parse(line):
        return list(map(lambda x: x.strip(), filter(None, re.split(r" {1,}", line))))

    lines = get_input(6).splitlines()
    operators = parse(lines[-1])
    res = list(map(lambda x: 1 if x == '*' else 0, operators))

    for i in range(len(lines) - 1):
        line = list(map(lambda x: int(x), parse(lines[i])))
        for j in range(len(operators)):
            res[j] = res[j] + line[j] if operators[j] == "+" else res[j] * line[j]

    return sum(res)


def part2() -> int:
    def compute(nums, op):
        nums = [int(''.join(num).strip()) for num in np.rot90(nums, 1)]
        if '*' in op: return functools.reduce(operator.mul, nums, 1)
        else: return functools.reduce(operator.add, nums, 0)

    lines = get_input(6).splitlines()
    operators = re.split(r'(?=\S)', lines[-1])[1:]
    offset = 0
    res = 0
    for i, op in enumerate(operators):
        if i == len(operators) - 1:
            nums = np.array([list(line[offset:]) for line in lines[0:-1]], dtype=np.chararray)
            res += compute(nums, op)
        else:
            size = len(op)
            nums = np.array([list(line[offset:offset+size-1]) for line in lines[0:-1]], dtype=np.chararray)
            res += compute(nums, op)
            offset += size

    return res



