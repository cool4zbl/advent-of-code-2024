import time
start_time = time.time()

is_test = False
day = 9
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

long_str = open(input_file).readline().strip()

res = []
file_id = 0
for i, c in enumerate(long_str):
    if i % 2:
        for k in range(int(c)):
            res.append('.')
    else:
        for k in range(int(c)):
            res.append(file_id)
        file_id += 1

left, right = 0, len(res) - 1
while left < right:
    while left < right and res[left] != '.':
        left += 1
    while right >= left and res[right] == '.':
        right -= 1
    if res[left] == '.' and res[right] != '.':
        res[right], res[left] = res[left], res[right]
    left += 1
    right -= 1


total = 0
for i in range(len(res)):
    if res[i] == '.':
        break
    total += i * res[i]

print(total)
print(f't2 = {time.time() - start_time:.6f}s')