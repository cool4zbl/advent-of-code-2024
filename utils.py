from typing import List

def read_integer_pairs(filepath: str) -> tuple[List[int], List[int]]:
    lst1, lst2 = [], []
    with open(filepath, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            lst1.append(left)
            lst2.append(right)
    return lst1, lst2

def read_file_to_list(filepath: str) -> List[int]:
    lst = []
    with open(filepath, 'r') as file:
        for line in file:
            lst.append([int(n) for n in line.strip().split(' ')])

    return lst