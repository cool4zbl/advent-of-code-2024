import re
import time

start_time = time.time()

is_test = False
day = 13
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def sol(input_file):
    pattern = r'X\+(\d+), Y\+(\d+)'
    pattern2 = r'X\=(\d+), Y\=(\d+)'
    total = 0
    with open(input_file) as f:
        items = f.read().split('\n\n')
        for item in items:
            l1, l2, l3 = item.split('\n')

            ms = re.findall(pattern, l1)
            x1, y1 = int(ms[0][0]), int(ms[0][1])
            ms = re.findall(pattern, l2)
            x2, y2 = int(ms[0][0]), int(ms[0][1])
            ms = re.findall(pattern2, l3)
            z1, z2 = int(ms[0][0]), int(ms[0][1])

            if x1 * y2 - x2 * y1 == 0:
                continue

            a = (z1 * y2 - x2 * z2) / (x1 * y2 - x2 * y1)
            b = (x1 * z2 - y1 * z1) / (x1 * y2 - x2 * y1)

            if int(a) == a and int(b) == b:
                total += int(a) * 3 + int(b) * 1
    print(total)
    return total

sol(input_file)