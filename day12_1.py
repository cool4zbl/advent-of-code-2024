from collections import defaultdict, deque
import time

start_time = time.time()

is_test = False
day = 12
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}, len(ls), len(ls[0])

g, m, n = build_grid(open(input_file, 'r').read().splitlines())

def find_non_adj(grid, r, c):
    count = 0
    for dx, dy in dirs:
        nr, nc = r + dx, c + dy
        if grid[nr, nc] and grid[nr, nc] == grid[r, c]:
            count += 1
    return 4 - count

def solve(grid):
    visited = set()
    total = 0

    def dfs(r, c, path):
        path.add((r, c))

        for dx, dy in dirs:
            nr, nc = r + dx, c + dy
            if grid[nr, nc] and grid[nr, nc] == grid[r, c] and (r + dx, c + dy) not in visited:
                visited.add((nr, nc))
                dfs(nr, nc, path)


    for r in range(m):
        for c in range(n):
            if (r, c) not in visited:
                path = set()
                dfs(r, c, path)
                area = len(path)
                per = 0
                for i, j in path:
                    per += find_non_adj(grid, i, j)
                total += area * per

    print('total', total)

solve(g)

