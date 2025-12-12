from utils.api import *

input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
input_str = get_input(1)

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    moves = input_str.split()
    pos = 50
    res = 0

    for move in moves:
        increment = int(move[1:]) * (-1 if move[0] == "L" else 1)
        pos = (pos + increment + 100) % 100
        if pos == 0: res += 1

    return res


def part2() -> int:
    moves = input_str.split()
    pos = 50
    res = 0

    for move in moves:
        increment = int(move[1:]) * (-1 if move[0] == "L" else 1)
        res += zero_passings(pos, increment, move[0])
        pos = (pos + increment + 100) % 100
        if pos == 0: res += 1

    return res


def zero_passings(pos, increment, dir):
    res = abs(int(increment/100))
    pos2 = pos + (increment + (res * (1 if dir == "L" else -1) * 100))
    if pos != 0 and (pos2 < 0 or pos2 > 100): res += 1
    return res