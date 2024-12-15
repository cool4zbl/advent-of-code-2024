from collections import defaultdict, deque
import time

# --- Day 12: Garden Groups ---

start_time = time.time()

is_test = False
day = 15
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

# U,D,L,R
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}, len(ls), len(ls[0])

def sol():
    p1, p2 = open(input_file, 'r').read().split('\n\n')
    lst = p1.splitlines()
    g, m, n = build_grid(lst)

    ACTS = ['^', 'v', '<', '>']

    actions = list(''.join(p2.split('\n')))
    print(actions)

    for k, v in g.items():
        if v == '@':
            sr, sc = k
            break
    print(sr, sc)

    r, c = sr, sc
    g[sr, sc] = '.'
    for action in actions:
        dr, dc = dirs[ACTS.index(action)]
        nr, nc = r + dr, c + dc

        if not g[nr, nc]:
            continue
        if g[nr, nc] == '#':
            continue
        elif g[nr, nc] == '.':
            r, c = nr, nc
        elif g[nr, nc] == 'O':
            if action == '>' or action == '<': # to right
                k = nc
                i = 0
                while (nr, nc + i * dc) in g:
                    if g[nr, nc + i * dc] == '#':
                        break
                    if g[nr, nc + i * dc] == '.':
                        k = nc + i * dc
                        break
                    i += 1
                if k != nc:
                    g[nr, k] = 'O'
                    g[nr, nc] = '.'
                    r, c = nr, nc

            elif action == 'v' or action == '^': # go down
                k = nr
                i = 0
                while (nr + i * dr, nc) in g:
                    if g[nr + i * dr, nc] == '#':
                        break
                    if g[nr + i * dr, nc] == '.':
                        k = nr + i * dr
                        break
                    i += 1
                if k != nr:
                    g[k, nc] = 'O'
                    g[nr, nc] = '.'
                    r, c = nr, nc

    total = 0
    for k, v in g.items():
        if v != 'O':
            continue
        x, y = k
        total += int(x) * 100 + int(y)

    print(total)

    board = [['.' for _ in range(n)] for _ in range(m)]
    for k, v in g.items():
        x, y = k
        board[x][y] = v
    for row in board:
        print(row)

sol()
