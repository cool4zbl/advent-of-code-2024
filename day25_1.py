from collections import defaultdict
import time

start_time = time.time()

is_test = False
day = 25
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

# UDLR
dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
acts = ['<', '>', '^', 'v']

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}, len(ls), len(ls[0])

def sol():
    schemas = open(input_file, 'r').read().split('\n\n')
    _locks = [s for s in schemas if s.startswith('#' * 5)]
    _keys = [s for s in schemas if s.startswith('.' * 5)]

    max_height = 7

    def get_heights(locks):
        lock_hs = []
        for lock in locks:
            lock = lock.split('\n')
            g, m, n = build_grid(lock)
            hs = [sum([1 if g[r, c] == '#' else 0 for r in range(m)]) for c in range(n)]

            lock_hs.append(hs)
        return lock_hs

    lock_hs = get_heights(_locks)
    key_hs = get_heights(_keys)

    total = sum([all(((x + y) <= max_height) for x, y in zip(locks, keys)) for keys in key_hs for locks in lock_hs])

    print(total)
sol()