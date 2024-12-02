from typing import List

def read_file_to_list(filepath: str) -> List[int]:
    lst = []
    with open(filepath, 'r') as file:
        for line in file:
            lst.append([int(n) for n in line.strip().split(' ')])

    return lst

def decreasing(lst):
    return all(
        (current > next_elem) and (1 <= (current - next_elem) <= 3)
        for current, next_elem in zip(lst, lst[1:])
    ) if len(lst) > 1 else True

def increasing(lst):
    return all(
        (current < next_elem) and (1 <= abs(current - next_elem) <= 3)
        for current, next_elem in zip(lst, lst[1:])
    ) if len(lst) > 1 else True

def reports():
    all_lst = read_file_to_list('./day2.txt')
    count = sum(map(lambda x: 1 if decreasing(x) or increasing(x) else 0, all_lst))
    return count

print('part1', reports())

def reports2():
    all_lst = read_file_to_list('./day2.txt')
    count = 0

    for lst in all_lst:
        if decreasing(lst) or increasing(lst):
            count += 1
        else:
            for i in range(len(lst)):
                removed_lst = lst[:i] + lst[i+1:]
                if decreasing(removed_lst) or increasing(removed_lst):
                    count += 1
                    break

    return count

print('part2', reports2())