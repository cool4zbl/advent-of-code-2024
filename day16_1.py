from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
import time

start_time = time.time()

is_test = False
day = 16
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

# UDLR
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
acts = ['^', 'v', '<', '>']

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}, len(ls), len(ls[0])

g, m, n = build_grid(open(input_file, 'r').read().splitlines())

def sol():
    sr, sc = next(k for k, v in g.items() if v == 'S')
    er, ec = next(k for k, v in g.items() if v == 'E')

    def dijkstra():
        open_list = [(0, sr, sc, 3)]
        heapify(open_list)
        closed_set = set()

        while open_list:
            score, r, c, d = heappop(open_list)

            if (r, c) in closed_set:
                continue
            closed_set.add((r, c))

            if (r, c) == (er, ec):
                return score

            for idx, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if g[nr, nc] and g[nr, nc] != '#':
                    new_score = score + (1001 if idx != d else 1)
                    heappush(open_list, (new_score, nr, nc, idx))
        return None

    print(dijkstra())

sol()