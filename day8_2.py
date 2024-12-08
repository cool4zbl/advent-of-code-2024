from collections import defaultdict

input_file = './input/day8.txt'

grid = {(x, y): e for x, line in enumerate(open(input_file).readlines()) for y, e in enumerate(line.strip())}

all_antennas = defaultdict(list)

for k, v in grid.items():
    if v not in '.#':
        all_antennas[v].append(k)

total = 0
uniq_antis = set()
for antenna, poss in all_antennas.items():
    for i in range(len(poss)):
        for j in range(i+1, len(poss)):
            x1, y1 = poss[i]
            x2, y2 = poss[j]

            a = (y1 - y2) / (x1 - x2)
            b = y1 - ((y1-y2) / (x1 - x2)) * x1
            uniq_antis.add((a, b))

for x, y in grid.keys():
    for a, b in uniq_antis:
        # left, right = (Decimal(str(a)) * Decimal(str(x)) + Decimal(str(b))), Decimal(str(y))
        left = a * x + b
        right = y
        if  abs(right - left) <= 0.0002:
            total += 1
            break

print(total)
