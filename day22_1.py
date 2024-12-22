import time

start_time = time.time()

is_test = False
day = 22
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

mod = 16777216
def hash_num(num):
    a = ((num * 64) ^ num) % mod
    b = ((a // 32) ^ a) % mod
    c = ((b * 2048) ^ b) % mod
    return c

def sol():
    nums = open(input_file, 'r').read().splitlines()
    res = []
    m = 2000

    for num in nums:
        hashed = int(num)
        for _ in range(m):
            hashed = hash_num(hashed)
        res.append(hashed)
    print(sum(res))

sol()

print(f'{(time.time() - start_time) * 1000:.3f}ms')

