import os

l = (
    x[3:5]
    for x in os.listdir("src")
    if "runner.py" not in x and ".py" in x and "__" not in x
)
l = list(l)
n = int(sorted(l)[-1][:2]) + 1 if len(l) > 0 else 1

DEFAULT_FILE = fr"""from utils.api import *

input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
# input_str = get_input({n})

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    res = 0
    return res


def part2() -> int:
    res = 0
    return res
"""

path = f"src/day{n:02d}.py"
with open(path, "w") as f:
    f.write(DEFAULT_FILE)

print(f"Enter your solution in {path}")
