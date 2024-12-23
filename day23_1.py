from collections import defaultdict
import time

start_time = time.time()

is_test = False
day = 23
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def sol():
    lines = open(input_file).read().splitlines()

    items = set()
    connects = defaultdict(set)
    for line in lines:
        a, b = line.strip().split('-')
        items.add(a)
        items.add(b)
        connects[a].add(b)
        connects[b].add(a)

    res = set()
    for k, v in connects.items():
        if k.startswith('t'):
            ll = list(v)
            for p in range(len(ll)):
                for q in range(p + 1, len(ll)):
                    if ll[q] in connects[ll[p]] and ll[p] in connects[ll[q]]:
                        res.add(hash(k) + hash(ll[p]) + hash(ll[q]))

    print('connected', len(res))

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
