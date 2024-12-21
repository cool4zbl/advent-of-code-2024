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

    g_small, m_small, n_small = build_grid(lst)

    # not for test
    board = [[] for _ in range(m_small)]
    for i, row in enumerate(board):
        for j in range(n_small):
            match g_small[i, j]:
                case '#':
                    row.append('#')
                    row.append('#')
                case '.':
                    row.append('.')
                    row.append('.')
                case 'O':
                    row.append('[')
                    row.append(']')
                case '@':
                    row.append('@')
                    row.append('.')

    g, m, n = build_grid(board)

    sr, sc = next(k for k, v in g.items() if v == '@')

    r, c = sr, sc
    g[sr, sc] = '.'

    actions = list(''.join(p2.split('\n')))

    def check(r, c, act, g):
        dr, dc = dirs[ACTS.index(act)]
        nr, nc = r + dr, c + dc

        if not g[nr, nc] or g[nr, nc] == '#':
            return False
        if g[nr, nc] == '.':
            return True
        if act in '<>':
            return check(nr, nc, act, g)

        if g[nr, nc] in '[]':
            lr = -1 if g[nr, nc] == ']' else 1
            # 如果下一步是 [ or ], 则递归移动上面的 [, ], 如果它们都成功移动了，说明我也可以移动到下一步的位置.
            return check(nr, nc, act, g) and check(nr, nc + lr, act, g)

    def move(r, c, act, g):
        dr, dc = dirs[ACTS.index(act)]
        nr, nc = r + dr, c + dc

        if g[nr, nc] != '.':
            if act in '<>':
                move(nr, nc, act, g)
            # 如果下一步是 [ or ], 则递归移动上面的 [, ], 如果它们都成功移动了，说明我也可以移动到下一步的位置.
            elif g[nr, nc] in '[]':
                lr = (-1 if g[nr, nc] == ']' else 1)
                move(nr, nc, act, g)
                move(nr, nc + lr, act, g)
        g[nr, nc] = g[r, c]
        g[r, c] = '.'
        return True

    for action in actions:
        dr, dc = dirs[ACTS.index(action)]
        nr, nc = r + dr, c + dc

        if check(r, c, action, g):
            move(r, c, action, g)
            r, c = nr, nc

    g[r, c] = '@'
    total = 0
    for k, v in g.items():
        if v != '[':
            continue
        x, y = k
        total += int(x) * 100 + int(y)

    print(total)

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
