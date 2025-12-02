from utils.api import *
from concurrent.futures import ThreadPoolExecutor, as_completed
import textwrap

input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
# input_str = get_input(2)

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    def check_range(ids):
        x, y = tuple(int(x) for x in ids.split("-"))
        res = 0

        for i in range(x, y + 1):
            i_ = str(i)
            if len(i_) % 2 == 0 and i_[:len(i_) // 2] == i_[len(i_) // 2:]:
                res += i

        return res

    ranges = get_input(2).split(",")
    l_tasks = []
    res = 0

    with ThreadPoolExecutor() as executor:
        for ids in ranges:
            l_tasks.append(executor.submit(check_range, ids))
        for task in as_completed(l_tasks):
            res += task.result()

    return res


def part2() -> int:
    def check_range(ids):
        x, y = tuple(int(x) for x in ids.split("-"))
        res = set()

        for i in range(x, y + 1):
            i_ = str(i)
            l_ = len(i_)
            for j in range(1, l_//2 + 1):
                elems = textwrap.wrap(i_, j)
                if all(z == elems[0] for z in elems):
                    res.add(i)

        return sum(res)


    ranges = get_input(2).split(",")
    l_tasks = []
    res = 0

    with ThreadPoolExecutor() as executor:
        for ids in ranges:
            l_tasks.append(executor.submit(check_range, ids))
        for task in as_completed(l_tasks):
            res += task.result()

    return res



