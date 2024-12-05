import time
import re
from collections import deque

start_time = time.time()

# --- Day 4: Ceres Search ---

def parse_file_to_matrix(filepath: str):
    lst = []
    with open(filepath, 'r') as file:
        for line in file:
            lst.append(line.strip())

    return lst


def find_xmas():
    board = parse_file_to_matrix('./input/day4.txt')
    m, n = len(board), len(board[0])

    count = 0
    # up, down, left, right,
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (1, -1), (-1, 1), (1, 1))

    word = 'XMAS'
    def dfs(row, col, idx, dir):
        if idx == len(word):
            return True

        if not (0 <= row < m and 0 <= col < n and word[idx] == board[row][col]):
            return False

        dr, dc = dir
        if dfs(dr + row, dc + col, idx + 1, dir):
            return True
        return False

    for i in range(m):
        for j in range(n):
            for dir in dirs:
                if dfs(i, j, 0, dir):
                    count += 1
    return count


print(find_xmas())
end1 = time.time()
print(f't = {end1 - start_time:.6f}s')

def check_board(cur, boards):
    re_boards = []
    for bd in boards:
        re_bd = [re.compile(pattern) for pattern in bd]
        re_boards.append(re_bd)

    for re_bd in re_boards:
        match_all = True
        for i in range(3):
            if not re_bd[i].match(cur[i]):
                match_all = False
                break
        if match_all:
            return True

    return False

def find_x_mas():
    board = parse_file_to_matrix('./input/day4.txt')
    m, n = len(board), len(board[0])

    pattern_xmas = ['M.S', '.A.', 'M.S']
    pattern_xmas_down = ['S.M', '.A.', 'S.M']
    pattern_xmas_left = ['M.M', '.A.', 'S.S']
    pattern_xmas_right = ['S.S', '.A.', 'M.M']

    count = 0
    for r in range(m):
        for c in range(n):
            if not ((0 <= r+2 < m) and (0 <= c+2 < n)):
                continue
            cur_board = [row[c:c+3] for row in board[r:r+3]]
            found = check_board(cur_board,
                                [pattern_xmas, pattern_xmas_down, pattern_xmas_left, pattern_xmas_right ])
            if found:
                count += 1

    return count


print(find_x_mas())
print(f't2 = {time.time() - end1:.6f}s')
