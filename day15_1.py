from collections import defaultdict, deque
import time

# --- Day 12: Garden Groups ---

start_time = time.time()

is_test = False
day = 15
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

# U,D,L,R
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
ACTS = ['^', 'v', '<', '>']

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}, len(ls), len(ls[0])

def sol():
    p1, p2 = open(input_file, 'r').read().split('\n\n')
    lst = p1.splitlines()
    g, m, n = build_grid(lst)
    actions = list(''.join(p2.split('\n')))

    sr, sc = next(k for k, v in g.items() if v == '@')

    r, c = sr, sc
    g[sr, sc] = '.'

    def check(r, c, act, g):
        dr, dc = dirs[ACTS.index(act)]
        nr, nc = r + dr, c + dc

        if not g[nr, nc] or g[nr, nc] == '#':
            return False
        if g[nr, nc] == '.':
            return True
        return check(nr, nc, act, g)

    def move(r, c, act, g):
        dr, dc = dirs[ACTS.index(act)]
        nr, nc = r + dr, c + dc

        if g[nr, nc] != '.':
            move(nr, nc, act, g)
        g[nr, nc] = g[r, c]
        g[r, c] = '.'
        return True

    def move_iterative(r, c, nr, nc):
        if not g[nr, nc] or g[nr, nc] == '#':
            return r, c
        elif g[nr, nc] == '.':
            return nr, nc
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
                    return nr, nc
                return r, c

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
                    return nr, nc
                return r, c

    for action in actions:
        dr, dc = dirs[ACTS.index(action)]
        nr, nc = r + dr, c + dc
        # r, c = move_iterative(r, c, nr, nc)

        if check(r, c, action, g):
            move(r, c, action, g)
            r, c = nr, nc

    total = 0
    for k, v in g.items():
        if v != 'O':
            continue
        x, y = k
        total += int(x) * 100 + int(y)

    print(total, total == 1515788)

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
