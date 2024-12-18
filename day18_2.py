from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
import time

start_time = time.time()

day = 18
is_test = False
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}

m = 7 if is_test else 71
n = 7 if is_test else 71
total_count = 12 if is_test else 1024

g = build_grid([['.' for i in range(n)] for j in range(m)])

def sol():
    def dijkstra(sr, sc, er, ec):
        open_list = [(0, sr, sc)]
        heapify(open_list)
        best_scores = defaultdict(int)
        best_scores[(sr, sc)] = 0
        closed_set = set()

        while open_list:
            score, r, c = heappop(open_list)
            closed_set.add((r, c))

            if best_scores[(r, c)] < score:
                continue

            if (r, c) == (er, ec):
                return score

            for idx, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if g[nr, nc] and g[nr, nc] != '#' and (nr, nc) not in closed_set:
                    new_score = score + 1
                    if (nr, nc) not in best_scores or new_score < best_scores[nr, nc]:
                        best_scores[nr, nc] = new_score
                        heappush(open_list, (new_score, nr, nc))
        return None

    with open(input_file, 'r') as f:
        count = 0
        for pos in f.read().splitlines():
            x, y = pos.split(',')
            x, y = int(y), int(x)
            g[x, y] = '#'
            if not dijkstra(0, 0, m-1, n-1):
                print('not found', y, x)
                break
            count += 1

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
