from collections import defaultdict, deque
import time

start_time = time.time()

is_test = False
day = 12
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

# U,D,L,R
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}, len(ls), len(ls[0])

g, m, n = build_grid(open(input_file, 'r').read().splitlines())

def calc_perimeter(grid, path):
    edges = set()

    for r, c in path:
        for i, (dx, dy) in enumerate(dirs):
            nr, nc = r + dx, c + dy
            if not grid[nr, nc] or grid[nr, nc] != grid[r, c]:
                edges.add((r, c, i))

    uniq_edges = set()
    for x, y, d in edges:
        if (x + 1, y, d) not in edges and (x, y + 1, d) not in edges:
            uniq_edges.add((x, y, d))

    return len(uniq_edges)

def solve(grid):
    visited = set()
    total = 0

    def dfs(r, c, path):
        path.append((r, c))
        visited.add((r, c))

        for dx, dy in dirs:
            nr, nc = r + dx, c + dy
            if grid[nr, nc] and grid[nr, nc] == grid[r, c] and (r + dx, c + dy) not in visited:
                visited.add((nr, nc))
                dfs(nr, nc, path)

    for r in range(m):
        for c in range(n):
            if (r, c) not in visited:
                path = []
                dfs(r, c, path)
                area = len(path)
                per = calc_perimeter(grid, path)
                total += area * per

    print('total', total)

solve(g)
print(f'time = {(time.time() - start_time) * 1000:.3f}ms')
