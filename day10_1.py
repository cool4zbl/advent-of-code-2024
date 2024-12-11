from collections import defaultdict
import time
start_time = time.time()

is_test = True
day = 10
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def parse_file(filepath: str):
    lst = []
    with open(filepath, 'r') as file:
        for line in file:
            lst.append([int(c) if c != '.' else '.' for c in list(line.strip())])

    return lst

board = parse_file(input_file)
m, n = len(board), len(board[0])

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

all_zeros = defaultdict(int)

word = '9876543210'
def dfs(row, col, idx, dir, er, ec):
    if idx == len(word):
        r = row - dir[0]
        c = col - dir[1]
        if (r, c) != (er, ec):
            return False
        return True

    if not (0 <= row < m and 0 <= col < n and int(word[idx]) == board[row][col]):
        return False

    char = board[row][col]
    board[row][col] = '#'
    is_found = False
    for dir in dirs:
        dr, dc = dir
        if dfs(dr + row, dc + col, idx + 1, dir, er, ec):
            is_found = True
            break
    board[row][col] = char
    return is_found

count = 0
nines = set()
for r in range(m):
    for c in range(n):
        if board[r][c] == 0:
            all_zeros[(r, c)] = 0
        if board[r][c] == 9:
            nines.add((r, c))

for r, c in all_zeros:
    for sr, sc in nines:
        er, ec = r, c
        if dfs(sr, sc, 0, 0, er, ec):
            all_zeros[(r, c)] += 1

print(sum(v for v in all_zeros.values()))
