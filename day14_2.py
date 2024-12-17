from collections import defaultdict, deque
import time

# --- Day 14: Restroom Redoubt ---

start_time = time.time()

is_test = False
day = 14
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def build_grid(m, n):
    return defaultdict(str) | {(i, j): 0 for i in range(m) for j in range(n)}

def sol():
    m, n = 103, 101

    # calculate maximum product of 4 quadrants?
    robots = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            p, v = line.split(' ')
            c, r = p.split('=')[1].split(',')
            vy, vx = v.split('=')[1].split(',')
            robots.append((int(r), int(c), int(vy), int(vx)))

    times = 7055
    # 5000 < x < 12500
    while times < 7056:
        g = build_grid(m, n)

        for robot in robots:
            sr, sc, vy, vx = robot
            er, ec = (sr + times * vx) % m, (sc + times * vy) % n
            g[(er, ec)] += 1

        found = True
        for k, v in g.items():
            x, y = k
            if v > 1:
                found = False
                break

        if found:
            print(found, times)

        board = [['.' for _ in range(n)] for _ in range(m)]
        for k, v in g.items():
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

        times += 1

sol()