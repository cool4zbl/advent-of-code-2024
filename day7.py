import time
start_time = time.time()

day = 7
is_test = False

# --- Day 7: Bridge Repair ---

def read_input():
    targets = []
    nums = []
    with open(f'./input/day{day}{"_test" if is_test else ""}.txt') as file:
        for line in file:
            target, ns = line.strip().split(':')
            targets.append(int(target.strip()))
            nums.append([int(n) for n in ns.strip().split()])
    return targets, nums

ops0 = '+*'
ops1 = '+*|'

def sol(targets, all_nums):

    def calc(target, total, idx, ops, nums):
        if idx >= len(nums):
            return total == target

        for op in ops:
            if op == '+':
                t = total + nums[idx]
                if calc(target, t, idx + 1, ops, nums):
                    return True
            elif op == '*':
                t = total * nums[idx]
                if calc(target, t, idx + 1, ops, nums):
                    return True
            elif op == '|':
                t = int(str(total) + str(nums[idx]))
                if calc(target, t, idx + 1, ops, nums):
                    return True
        return False

    total0 = 0
    total1 = 0

    for target, ns in zip(targets, all_nums):
        if calc(target, ns[0], 1, ops0, ns):
            total0 += target
        if calc(target, ns[0], 1, ops1, ns):
            total1 += target
    return total0, total1

if __name__ == "__main__":
    targets, nums = read_input()
    print(sol(targets, nums))
    print(f'time = {(time.time() - start_time):.6f}s')
