import time

start_time = time.time()

day = 17
is_test = False
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def run(programs, register_a, register_b, register_c):
    opcode_p = 0
    output = []

    def get_operand(operand_pointer):
        cur_v = int(programs[operand_pointer])
        if 0 <= cur_v <= 3:
            return cur_v
        if cur_v == 4:
            return register_a
        if cur_v == 5:
            return register_b
        if cur_v == 6:
            return register_c
        return cur_v

    while opcode_p + 1 < len(programs):
        operand_p = opcode_p + 1
        opcode = programs[opcode_p]
        if opcode == '0':
            v = get_operand(operand_p)
            # adv
            register_a = register_a // (2 ** v)
            # print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')
        elif opcode == '1':
            # bxl
            register_b ^= int(programs[operand_p])
            # print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')
        elif opcode == '2':
            v = get_operand(operand_p)
            # bst
            register_b = v % 8
            # print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')
        elif opcode == '3':
            if register_a != 0:
                # jnz
                v = get_operand(operand_p)
                opcode_p = v
                operand_p = opcode_p + 1
                # print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}, jnz = {opcode_p}')
                continue
            # print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}, jnz no')
        elif opcode == '4':
            # bxc
            register_b ^= register_c
            # print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')
        elif opcode == '5':
            # out
            v = get_operand(operand_p)
            # format_v = ','.join(list(str(v % 8)))
            output.append(str(v % 8))
            print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}, output = {output})')
        elif opcode == '6':
            # bdv
            v = get_operand(operand_p)
            register_b = register_a // (2 ** v)
            # print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')
        elif opcode == '7':
            # cdv
            v = get_operand(operand_p)
            register_c = register_a // (2 ** v)
            # print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')

        opcode_p += 2
        operand_p = opcode_p + 1

    return output

def solve_part_1():
    with open(input_file) as f:
        p1, p2 = f.read().split('\n\n')
        lines = p1.split('\n')
        register_a = int(lines[0].split(':')[1].strip())
        register_b = int(lines[1].split(':')[1].strip())
        register_c = int(lines[2].split(':')[1].strip())

        programs = p2.split(':')[1].strip().split(',')
        return run(programs, register_a, register_b, register_c)

def sol_part_2():
    with open(input_file) as f:
        _, p2 = f.read().split('\n\n')
        program = p2.split(':')[1].strip().split(',')

        N = len(program)
        min_A = 8 ** (N - 1)
        bytes_a = [int(n) for n in oct(min_A)[2:]]

        idx = 0
        while idx < N:
            bytes_a[idx] += 1

            if bytes_a[idx] > 7:
                bytes_a[idx] = 0
                idx -= 1
                continue

            A = int(''.join([str(n) for n in bytes_a]), 8)
            output = run(program, A, 0, 0)

            # the last number of output would be generated from the most significant bits from registerA
            if output[N - 1 - idx] == program[N - 1 - idx]:
                print(f'found A = {A}, idx={idx}')
                idx += 1

            if idx == -1:
                print('no result')
                break

        if idx == N:
            print('all pass', A)
        else:
            print('all fail')

# 8 ** 15 < A < 8 ** 16 (281474976710656)
sol_part_2()
print(f'time = {(time.time() - start_time) * 1000:.3f}ms')
