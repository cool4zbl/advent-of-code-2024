from collections import defaultdict
import time

start_time = time.time()

is_test = True
day = 22
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

mod = 16777216
def hash_num(n):
    hashed = [n]
    for _ in range(2000):
        n = ((n * 64) ^ n) % mod
        n = ((n // 32) ^ n) % mod
        n = ((n * 2048) ^ n) % mod
        hashed.append(n)
    return hashed

def sol():
    nums = open(input_file, 'r').read().splitlines()
    sequence = defaultdict(int)

    for i, num in enumerate(nums):
        prices = [(x % 10) for x in hash_num(int(num))]
        diffs = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        seen = {}

        for j in range(len(diffs) - 3):
            s = tuple(diffs[j: j + 4])
            if s not in seen:
                seen[s] = prices[j + 4]
        for s, price in seen.items():
            sequence[s] += price

    print(max(sequence.values()))

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
