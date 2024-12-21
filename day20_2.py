from collections import defaultdict
from heapq import heappush, heappop, heapify
from utils import *
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

    dijkstra(sr, sc, er, ec)

    path = construct_path(parents, [], sr, sc, er, ec)

    # save-secs, positions
    cheats = defaultdict(set)
    for i, (x1, y1) in enumerate(path):
        for j in range(i + 1, len(path)):
            x2, y2 = path[j]

            duration = abs(x2 - x1) + abs(y2 - y1)
            if duration <= 20:
                fast = j - i - duration
                cheats[fast].add((x1, y1, x2, y2))

    total = 0
    for k, v in cheats.items():
        total += len(v) if k >= 100 else 0
    print('total', total)

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
