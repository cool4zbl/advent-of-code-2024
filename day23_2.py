from collections import defaultdict
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

    r, x = set(), set()

    res = []
    # see https://oi-wiki.org/graph/max-clique/
    def bron(R, P, X):
        if not P and not X:
            res.append(R.copy())
            return

        for v in list(P):
            bron(R | {v}, P & connects[v], X & connects[v])
            P.remove(v)
            X.add(v)

    print('connected', len(points))
    bron(r, points, x)
    max_n, computers = max((len(r), r) for r in res)
    computers = sorted(list(computers))
    print(max_n, ','.join(computers))

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
