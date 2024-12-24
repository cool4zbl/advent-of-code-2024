from collections import defaultdict
import time

start_time = time.time()

is_test = False
day = 24
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def sol():
    p1, p2 = open(input_file).read().split('\n\n')
    wires = defaultdict(int)
    for line in p1.splitlines():
        wire, v = line.split(': ')
        wires[wire] = int(v)

    relations = defaultdict()
    for line in p2.splitlines():
        w0, op, w1, _, w2 = line.split(' ')
        relations[w2] = (w0, op, w1)
    print(relations)

    def get_value(relation):
        # print('relation', relation)
        w, re = relation
        if w in wires:
            return wires[w]

        w0, op, w1 = re
        v1 = wires[w0] if w0 in wires else get_value((w0, relations[w0]))
        v2 = wires[w1] if w1 in wires else get_value((w1, relations[w1]))

        match op:
            case 'XOR':
                return v1 ^ v2
            case 'AND':
                return v1 & v2
            case 'OR':
                return v1 | v2


    for relation in relations.items():
        k, re = relation
        v = get_value(relation)
        wires[k] = v

    zs = [w for w in wires.keys() if w.startswith('z')]
    zs.sort(reverse=True)
    bin_o = ''.join([str(wires[k]) for k in zs])
    print(int(bin_o, 2))

sol()
