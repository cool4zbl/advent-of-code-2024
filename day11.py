from collections import defaultdict
from functools import lru_cache
import time

day = 11
is_test = False
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def read_input(filepath):
    return open(filepath, 'r').readline().strip().split()

def remove_leading_zero(ns):
    stripped = ns.lstrip('0')
    return '0' if not stripped else stripped

cache = defaultdict(dict)

def process(num, ts):
    if ts <= 0:
        return 1

    if cache[num].get(ts):
        return cache[num][ts]

    if num == '0':
        stones = process('1', ts - 1)

    elif len(num) % 2 == 0:
        mid = len(num) // 2
        n1, n2 = remove_leading_zero(num[:mid]), remove_leading_zero(num[mid:])
        stones = process(n1, ts - 1) + process(n2, ts - 1)
    else:
        temp = str(int(num) * 2024)
        stones = process(temp, ts - 1)

    cache[num][ts] = stones
    return cache[num][ts]

@lru_cache(maxsize=None)
def process_with_cache(num, ts):
    if ts <= 0:
        return 1

    if num == '0':
        return process_with_cache('1', ts - 1)

    if len(num) % 2 == 0:
        mid = len(num) // 2
        n1, n2 = remove_leading_zero(num[:mid]), remove_leading_zero(num[mid:])
        stones = process_with_cache(n1, ts - 1) + process_with_cache(n2, ts - 1)
    else:
        temp = str(int(num) * 2024)
        stones = process_with_cache(temp, ts - 1)

    return stones


def main():
    start_time = time.time()

    times = 75
    init_lst = read_input(input_file)
    # total = sum(process(num, times) for num in init_lst)
    total = sum(process_with_cache(num, times) for num in init_lst)
    print(total)
    print(f'time spent = {(time.time() - start_time) * 1000:.3f} ms')

if __name__ == '__main__':
    main()