from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
import time

start_time = time.time()

is_test = True
day = 16
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

# UDLR
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
acts = ['^', 'v', '<', '>']

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}, len(ls), len(ls[0])

g, m, n = build_grid(open(input_file, 'r').read().splitlines())

def sol():
    for k, v in g.items():
        if v == 'S':
            sr, sc = k
        if v == 'E':
            er, ec = k

    def dijkstra():
        open_list = [(0, sr, sc, 3)]
        heapify(open_list)
        best_scores = defaultdict(int)
        best_scores[(sr, sc)] = 0
        closed_set = set()

        while open_list:
            score, r, c, d = heappop(open_list)
            closed_set.add((r, c))
            g[r, c] = acts[d]

            if best_scores[(r, c)] < score:
                continue

            if (r, c) == (er, ec):
                return score

            for idx, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if g[nr, nc] and g[nr, nc] != '#' and (nr, nc) not in closed_set:
                    new_score = score + (1001 if idx != d else 1)
                    if (nr, nc) not in best_scores or new_score < best_scores[nr, nc]:
                        best_scores[nr, nc] = new_score
                        heappush(open_list, (new_score, nr, nc, idx))
        return None

    print(dijkstra())

sol()

board = [['.' for _ in range(n)] for _ in range(m)]
for k, v in g.items():
    x, y = k
    board[x][y] = v

for row in board:
    print(''.join(row))

