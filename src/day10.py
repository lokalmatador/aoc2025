from utils.api import *
import numpy as np
import re
from itertools import chain, combinations
from scipy.optimize import milp, LinearConstraint, Bounds


input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
# input_str = get_input(10)

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    machines = get_input(10).splitlines()

    res = 0
    for machine in machines:
        res += find_buttons1(machine)

    return res


def find_buttons1(machine):
    items = machine.split(" ")
    goal = np.array(list(map(lambda x: True if x == "#" else False, items[0][1:-1])))
    buttons = list(map(lambda x: tuple(map(int, re.findall(r'[0-9]+', x))), items[1:-1]))

    res = len(buttons) + 1
    for combo in chain.from_iterable(combinations(buttons, r) for r in range(len(buttons) + 1)):
        cur = np.array([False] * len(goal))
        steps = 0
        for button in combo:
            steps += 1
            for b in button:
                cur[b] = not cur[b]

        if (cur == goal).all() and steps < res:
            res = steps

    return res


def part2() -> int:
    machines = get_input(10).splitlines()

    res = 0
    for machine in machines:
        res += find_buttons2(machine)

    return res


def find_buttons2(machine):
    items = machine.split(" ")
    joltages = np.array(list(map(lambda x: int(x), items[-1][1:-1].split(","))))
    buttons = list(map(lambda x: tuple(map(int, re.findall(r'[0-9]+', x))), items[1:-1]))
    n = len(joltages)
    m = len(buttons)

    A = np.zeros((n, m), dtype=int)
    for j, inds in enumerate(buttons):
        for i in inds:
            A[i, j] = 1
    c = np.ones(m, dtype=float)

    joltages = np.array(joltages, dtype=float)
    lc = LinearConstraint(A, lb=joltages, ub=joltages)
    bounds = Bounds(lb=np.zeros(m), ub=np.full(m, np.inf))
    integrality = np.ones(m, dtype=int)
    res = milp(c=c, constraints=[lc], integrality=integrality, bounds=bounds)

    if res.status != 0:
        raise RuntimeError(f"ILP failed with status {res.status}: {res.message}")

    return int(round(res.fun))
