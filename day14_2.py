from collections import defaultdict, deque
import time

# --- Day 12: Garden Groups ---

start_time = time.time()

is_test = False
day = 14
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

# m, n = 7, 11

def build_grid(m, n):
    return defaultdict(str) | {(i, j): 0 for i in range(m) for j in range(n)}

def sol():
    m, n = 103, 101

    for times in range(2):
        g = build_grid(m, n)
        robots = []

        with open(input_file, 'r') as f:
            for line in f.readlines():
                p, v = line.split(' ')
                c, r = p.split('=')[1].split(',')
                vy, vx = v.split('=')[1].split(',')
                robots.append((int(r), int(c), int(vy), int(vx)))

        for robot in robots:
            sr, sc, vy, vx = robot
            er, ec = (sr + times * vx) % m, (sc + times * vy) % n
            g[(er, ec)] += 1

        board = [['.' for _ in range(n)] for _ in range(m)]
        for k,v in g.items():
            x, y = k
            board[x][y] = str(v) if v > 0 else '.'

        output = ""
        for row in board:
            output += ''.join(row)
            output += '\n'

        filepath = f'input/day14_pics/{times}.txt'

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(output)

        print(f'Saved output to {filepath}')

sol()