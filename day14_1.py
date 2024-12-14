from collections import defaultdict, deque
import time

# --- Day 12: Garden Groups ---

start_time = time.time()

is_test = False
day = 14
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

m = 103
n = 101
times = 100
def build_grid():
    return defaultdict(str) | {(i, j): 0 for i in range(m) for j in range(n)}

g = build_grid()

def sol():
    robots = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            p, v = line.split(' ')
            c, r = p.split('=')[1].split(',')
            vy, vx = v.split('=')[1].split(',')
            robots.append((int(r), int(c), int(vy), int(vx)))

    print('robots', robots)

    for robot in robots:
        sr, sc, vy, vx = robot
        er, ec = (sr + times * vx) % m, (sc + times * vy) % n
        print(er, ec)
        g[(er, ec)] += 1

    res = defaultdict(int)
    for k, v in g.items():
        x, y = k
        if x == m // 2 or y == n // 2 or v == 0:
            continue

        if x > m // 2:
            x = (x - 1)
        if y > n // 2:
            y = (y - 1)
        quadrant = (x // (m // 2), y // (n // 2))
        res[quadrant] += v

    total = 1
    for v in res.values():
        total *= v
    print(total)

sol()