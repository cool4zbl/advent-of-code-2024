import time

start_time = time.time()

day = 17
is_test = True
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def solve_part_1():
    with open(input_file) as f:
        p1, p2 = f.read().split('\n\n')
        lines = p1.split('\n')
        register_a = int(lines[0].split(':')[1].strip())
        register_b = int(lines[1].split(':')[1].strip())
        register_c = int(lines[2].split(':')[1].strip())

        programs = p2.split(':')[1].strip().split(',')

        # opcode,operand
        opcode_p = 0
        operand_p = 1

        output = []

        def get_operand(operand_pointer):
            cur_v = int(programs[operand_pointer])
            if 0 <=  cur_v <= 3:
                return  cur_v
            if  cur_v == 4:
                return register_a
            if  cur_v == 5:
                return register_b
            if  cur_v == 6:
                return register_c
            return  cur_v

        while operand_p < len(programs):
            opcode = programs[opcode_p]
            if opcode == '0':
                v = get_operand(operand_p)
                # adv
                register_a = register_a // (2 ** v)
                print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')
            elif opcode == '1':
                # v = get_operand(operand_p), DO NOT need to translate!!!
                # bxl
                register_b ^= int(programs[operand_p])
                print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')
            elif opcode == '2':
                v = get_operand(operand_p)
                # bst
                register_b = v % 8
                print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')
            elif opcode == '3':
                if register_a != 0:
                    # jnz
                    v = get_operand(operand_p)
                    opcode_p = v
                    operand_p = opcode_p + 1
                    print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}, jnz = {opcode_p}')
                    continue
                print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}, jnz no')
            elif opcode == '4':
                # bxc
                register_b ^= register_c
                print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')
            elif opcode == '5':
                # out
                v = get_operand(operand_p)
                format_v = ','.join(list(str(v % 8)))
                output.append(format_v)
                print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}, output = {output})')
            elif opcode == '6':
                # bdv
                v = get_operand(operand_p)
                register_b = register_a // (2 ** v)
                print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')
            elif opcode == '7':
                # cdv
                v = get_operand(operand_p)
                register_c = register_a // (2 ** v)
                print(f'a = {register_a}, b = {register_b}, c = {register_c}, i = {opcode_p}')

            opcode_p += 2
            operand_p = opcode_p + 1

        return ','.join(output)

print(solve_part_1())



