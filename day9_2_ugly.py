import time
start_time = time.time()

is_test = False
day = 9
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

long_str = open(input_file).readline().strip()

r = []
file_id = 0
dot_idx = []
id_idx = []
all_count = 0
for i, c in enumerate(long_str):
    if i % 2:
        for k in range(int(c)):
            r.append('.')
        dot_idx.append([all_count, int(c)])
        all_count += int(c)
    else:
        for k in range(int(c)):
            r.append(file_id)
        id_idx.append([file_id, int(c)])
        file_id += 1
        all_count += int(c)

# print(r)

left, right = 0, len(r) - 1
right = len(r) - 1
while right > 0:
    while r[right] == '.':
        right -= 1
    count = 1
    while right > 0 and r[right] == r[right-1]:
        right -= 1
        count += 1
    for i, (dot_index, l_dot) in enumerate(dot_idx):
        if l_dot >= count and dot_index < right:
            r[dot_index: count+dot_index], r[right:right+count] = r[right:right+count], r[dot_index: count+dot_index]
            dot_idx[i] = [dot_index + count, l_dot - count]
            break
    right -= 1


total = 0
for i in range(len(r)):
    if r[i] != '.':
        total += i * r[i]

print(total)
print(f't2 = {time.time() - start_time:.6f}s')