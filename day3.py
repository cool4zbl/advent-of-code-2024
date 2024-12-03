import re

pattern1 = r'mul\((\d{1,3}),(\d{1,3})\)'
pattern = r'mul\((\d{1,3}),(\d{1,3})\)|don\'t\(\)|do\(\)'

def sol():
    with open('./input/day3.txt', 'r') as file:
        total = 0
        for line in file:
            ms = re.findall(pattern1, line)
            total += sum([int(x) * int(y) for x, y in ms])
    return total

print(sol())

def sol2():
    with open('./input/day3.txt', 'r') as file:
        total = 0
        enable = True # it's global scope, not line-scope

        for line in file:
            for match in re.finditer(pattern, line):
                if match[0] == 'don\'t()':
                    enable = False
                elif match[0] == 'do()':
                    enable = True
                elif enable:
                    total += int(match[1]) * int(match[2])
    return total

print(sol2())