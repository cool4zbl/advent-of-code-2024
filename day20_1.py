from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
import time

start_time = time.time()

is_test = False
day = 20
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

# UDLR
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
acts = ['^', 'v', '<', '>']

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}, len(ls), len(ls[0])

def sol():

    g, m, n = build_grid(open(input_file, 'r').read().splitlines())
    sr, sc = next(k for k, v in g.items() if v == 'S')
    er, ec = next(k for k, v in g.items() if v == 'E')
    parents = defaultdict(tuple)

    def dijkstra(sr, sc, er, ec):
        open_list = [(0, sr, sc, 0)]
        heapify(open_list)
        closed_set = set()
        parents[sr, sc] = (sr, sc)

        while open_list:
            score, r, c, d = heappop(open_list)

            if (r, c) in closed_set:
                continue
            closed_set.add((r, c))
            if (r, c) != (sr, sc):
                parents[r, c] = (r - dirs[d][0], c - dirs[d][1])

            if (r, c) == (er, ec):
                return score

            for idx, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if g[nr, nc] and g[nr, nc] != '#':
                    new_score = score + 1
                    heappush(open_list, (new_score, nr, nc, idx))
        return None

    best = dijkstra(sr, sc, er, ec)
    print('best', best)

    path = []
    def construct_path(p, path):
        r, c = er, ec
        while (r, c) != (sr, sc):
            path.append((r, c))
            r, c = p[r, c]
        path.append((r, c))
        return path

    construct_path(parents, path)
    path.reverse()

    # save-secs, positions
    cheats = defaultdict(set)
    for i, (x, y) in enumerate(path):
        for idx, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy
            n2x, n2y = nx + dx, ny + dy
            if g[nx, ny] and g[nx, ny] == '#' and g[n2x, n2y] and g[n2x, n2y] != '#':
                pos = path.index((n2x, n2y))
                if pos < i:
                    continue
                fast = pos - i - 2
                cheats[fast].add((nx, ny, n2x, n2y))

    total = 0
    for k, v in cheats.items():
        total += len(v) if k >= 100 else 0
    print('total', total)
    # board = [['.' for _ in range(n)] for _ in range(m)]
    # for k, v in g.items():
    #     x, y = k
    #     board[x][y] = v if k not in path else 'O'
    #
    # for row in board:
    #     print(''.join(row))

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
