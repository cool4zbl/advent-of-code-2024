from collections import defaultdict
from typing import List

def read_integer_pairs(filepath: str) -> tuple[List[int], List[int]]:
    lst1, lst2 = [], []

    with open(filepath, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            lst1.append(left)
            lst2.append(right)
    return lst1, lst2

def parse_file_to_int_list(filepath: str) -> List[List[int]]:
    lst = []
    with open(filepath, 'r') as file:
        for line in file:
            lst.append([int(n) for n in line.strip().split(' ')])

    return lst

def parse_file_to_matrix(filepath: str):
    lst = []
    with open(filepath, 'r') as file:
        for line in file:
            lst.append(line.strip())

    return lst

def parse_file_to_2d_matrix(filepath: str):
    lst = []
    with open(filepath, 'r') as file:
        for line in file:
            lst.append(list(line.strip()))

    return lst

def print_board(board):
    for line in board:
        print(''.join(line))

def construct_path(parents, path, start_r, start_c, end_r, end_c):
    r, c = end_r, end_c
    while (r, c) != (start_r, start_c):
        path.append((r, c))
        r, c = parents[r, c]
    path.append((r, c))
    path.reverse()
    return path

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}, len(ls), len(ls[0])
