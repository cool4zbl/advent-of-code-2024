from collections import defaultdict, deque
import time

start_time = time.time()

is_test = False
day = 10
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}

grid = build_grid(open(input_file, 'r').read().splitlines())

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

all_zeros = [x for x in grid if grid[x] == '0']
q = deque()
for zero_pos in all_zeros:
    q.append(zero_pos)

total = 0
while q:
    (r, c) = q.popleft()
    if grid[(r, c)] == '9':
        total += 1
        continue

    for dx, dy in dirs:
        nr, nc = r + dx, c + dy
        if (nr, nc) in grid and int(grid[nr, nc]) == int(grid[r, c]) + 1:
            q.append((nr, nc))

print(total)
print(f'time {time.time() - start_time:.6f}s')
