from utils.api import *

input_str = get_test_input()
# UNCOMMENT THE FOLLOWING LINE TO READ THE ACTUAL INPUT
input_str = get_input(3)

# WRITE YOUR SOLUTION HERE

def part1() -> int:
    racks = input_str.split()
    res = 0

    for rack in racks:
        batteries = list(rack)
        res += int(find_largest_number(batteries, 2))

    return res


def part2() -> int:
    racks = input_str.split()
    res = 0

    for rack in racks:
        batteries = list(rack)
        res+=int(find_largest_number(batteries, 12))

    return res


def find_largest_number(arr, n, memo={}):
    if n == 0: return ""
    if not arr: return None

    key = (tuple(arr), n)
    if key in memo: return memo[key]

    largest_number = None
    for i in range(len(arr)):
        remaining_arr = arr[i+1:]
        remaining_number = find_largest_number(remaining_arr, n-1, memo)

        if remaining_number is not None:
            current_number = str(arr[i]) + str(remaining_number)
            if largest_number is None or current_number > largest_number:
                largest_number = current_number

    memo[key] = largest_number

    return largest_number
