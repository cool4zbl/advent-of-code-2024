from collections import defaultdict
from utils import parse_file_to_2d_matrix
import time
start_time = time.time()

is_test = False
day = 10
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

# grid = [(x, y) for x, line in enumerate(open(input_file).readlines()) for y, e in enumerate(line.strip())]
def parse_file(filepath: str):
    lst = []
    with open(filepath, 'r') as file:
        for line in file:
            lst.append([int(c) if c != '.' else '.' for c in list(line.strip())])

    return lst

board = parse_file(input_file)
m, n = len(board), len(board[0])

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

# word = '0123456789'
all_zeros = defaultdict(int)
word = '9876543210'
def find_all_paths(matrix, sx, sy, ex, ey):
    rows, cols = len(matrix), len(matrix[0])
    all_paths = []

    def is_valid(x, y, visited, idx):
        return 0 <= x < rows and 0 <= y < cols and (matrix[x][y]) == int(word[idx]) and (x, y) not in visited

    def dfs(x, y, path, visited, idx):
        if idx == len(word) - 1:
            if (x, y) == (ex, ey):
                all_paths.append(path.copy())
            return

        visited.add((x, y))

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            valid = is_valid(nx, ny, visited, idx + 1)
            if valid:
                path.append((nx, ny))
                dfs(nx, ny, path, visited, idx + 1)
                path.pop()

        visited.remove((x, y))

    dfs(sx, sy, [(sx, sy)], set(), 0)

    return all_paths

# def dfs(row, col, idx, dir, er, ec):
#     if idx == len(word):
#         r = row - dir[0]
#         c = col - dir[1]
#         # all_zeros[(r, c)] += 1
#         if (r, c) != (er, ec):
#             return False
#         return True

#     if not (0 <= row < m and 0 <= col < n and int(word[idx]) == board[row][col]):
#         return False

#     char = board[row][col]
#     board[row][col] = '#'
#     is_found = False
#     for dir in dirs:
#         dr, dc = dir
#         dfs(dr + row, dc + col, idx + 1, dir, er, ec)
#             # continue
#     board[row][col] = char
#     return False

count = 0
nines = set()
for r in range(m):
    for c in range(n):
        if board[r][c] == 0:
            all_zeros[(r, c)] = 0
        if board[r][c] == 9:
            nines.add((r, c))

print(board)
for r, c in all_zeros:
    for sr, sc in nines:
        er, ec = r, c
        paths = find_all_paths(board, sr, sc, er, ec)
        rating = len(paths)
        if rating > 0:
            all_zeros[(r, c)] += rating

print(all_zeros)
print(sum(v for v in all_zeros.values()))
