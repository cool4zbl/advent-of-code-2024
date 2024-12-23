import queue
from collections import defaultdict, deque
import time

start_time = time.time()

is_test = False
day = 23
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def sol():
    lines = open(input_file).read().splitlines()

    points = set()
    connects = defaultdict(set)
    for line in lines:
        a, b = line.strip().split('-')
        points.add(a)
        points.add(b)
        connects[a].add(b)
        connects[b].add(a)

    cliques = set()
    ps = sorted(list(points))
    def backtrack(group, candidates, start):
        cliques.add(frozenset(group))

        for i in range(start, len(candidates)):
            p = candidates[i]
            if all((p in connects[v]) for v in group):
               backtrack(group | {p}, candidates, i + 1)

    backtrack(set(), ps, 0)

    print(max((len(r), ','.join(sorted(r))) for r in cliques))

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
