from collections import defaultdict, deque
from utils import build_grid
import time

day = 6
is_test = True
input_file = f'./input/day{day}{'_test' if is_test else ''}.txt'

start_time = time.time()

# URDL
dirs = ((-1, 0), (0, 1),  (1, 0), (0, -1))
acts = ('^', '>', 'v', '<')
# U -> R, R -> D, D -> L, L -> U

def sol_part_1():
    lst = open(input_file, 'r').read().splitlines()
    g, m, n = build_grid(lst)

    start_pos = next(k for k, v in g.items() if v == '^')
    print(f'Part 1: {start_pos}')

    def bfs():
        q = deque([(start_pos, 0)])
        while q:
            (x, y), idx_d = q.popleft()
            visited.add((x, y))

            d = dirs[idx_d]
            nx, ny = x + d[0], y + d[1]
            if (nx, ny) not in g:
                print(f'Part 1: {nx}, {ny} not in g, break now')
                break
            if g[nx, ny] != '#':
                q.append(((nx, ny), idx_d))
            else:
                q.append(((x, y), (idx_d + 1) % 4))

    visited = { start_pos }
    def dfs(x, y, idx_d, g):
        if not g[(x, y)]:
            return
        visited.add((x, y))

        nx, ny = x + dirs[idx_d][0], y + dirs[idx_d][1]
        if g[nx, ny] == '#':
            dfs(x, y, (idx_d + 1) % 4, g)
        else:
            dfs(nx, ny, idx_d, g)

    dfs(start_pos[0], start_pos[1], 0, g)

    return len(visited)

print(sol_part_1())
print(f'time = {(time.time() - start_time) * 1000:.3f}ms')
