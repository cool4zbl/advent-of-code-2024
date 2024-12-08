from collections import defaultdict
from utils import parse_file_to_2d_matrix, print_board

grid = {(x, y): e for x, line in enumerate(open('./input/day8_test.txt').readlines()) for y, e in enumerate(line.strip())}

all_antennas = defaultdict(list)

for k, v in grid.items():
    if v not in '.':
        all_antennas[v].append(k)

total = 0
uniq_antis = set()
for antenna, poss in all_antennas.items():
    for i in range(len(poss)):
        for j in range(i+1, len(poss)):
            x1, y1 = poss[i]
            x2, y2 = poss[j]

            d_x = (x1 - x2)
            d_y = (y1 - y2)

            anti1 = (x1 + d_x, y1 + d_y)
            if anti1 in grid:
                if anti1 not in uniq_antis:
                    uniq_antis.add(anti1)
                    total += 1

            anti2 = (x2 - d_x, y2 - d_y)
            if anti2 in grid:
                if anti2 not in uniq_antis:
                    uniq_antis.add(anti2)
                    total += 1

print(total)

mat = parse_file_to_2d_matrix('./input/day8_test.txt')
for x, y in uniq_antis:
    mat[x][y] = '#'
print_board(mat)
