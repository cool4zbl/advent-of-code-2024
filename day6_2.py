from utils import build_grid
import time

day = 6
is_test = False
input_file = f'./input/day{day}{'_test' if is_test else ''}.txt'

start_time = time.time()

# URDL
dirs = ((-1, 0), (0, 1),  (1, 0), (0, -1))
acts = ('^', '>', 'v', '<')
# U -> R, R -> D, D -> L, L -> U

def sol_part_2():
    lst = open(input_file, 'r').read().splitlines()
    g, m, n = build_grid(lst)

    start_pos = next(k for k, v in g.items() if v == '^')

    visited = set()
    obstacles = set()
    path = set()

    x, y = start_pos
    idx_d = 0

    while (x, y) in g:
        visited.add(((x, y), idx_d))
        path.add((x, y))
        d = dirs[idx_d]
        nx, ny = x + d[0], y + d[1]
        if (nx, ny) in g and g[nx, ny] == '#':
            idx_d = (idx_d + 1) % 4
        else:
            obs = (nx, ny)
            if obs in g and obs not in path:
                check_loop(x, y, idx_d, obs, obstacles, visited.copy(), g)
            x, y = nx, ny

    return len(path), len(obstacles)

def check_loop(x, y, idx_d, obs, obstacles, visited, g):
    n_pos = (x, y)
    n_dir = idx_d
    while n_pos in g:
        visited.add((n_pos, n_dir))
        d = dirs[n_dir]
        nxt = (n_pos[0] + d[0], n_pos[1] + d[1])
        if nxt in g and g[nxt] == '#' or nxt == obs:
            n_dir = (n_dir + 1) % 4
        else:
            n_pos = nxt
        if (n_pos, n_dir) in visited:
            obstacles.add(obs)
            break

print(sol_part_2())
print(f'time = {(time.time() - start_time) * 1000:.3f}ms')