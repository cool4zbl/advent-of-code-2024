from collections import defaultdict
import time
from functools import cache
from heapq import heapify, heappop, heappush


start_time = time.time()

is_test = True
day = 21
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

# UDLR
# dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
# acts = ['^', 'v', '<', '>' ]
# #
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
acts = [ '^', '>',  'v', '<']

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}, len(ls), len(ls[0])

def sol():
    g, m, n = build_grid([list('789'), list('456'), list('123'), list('#0A')])
    g2, _, _ = build_grid([list('#^A'), list('<v>')])

    def find_path(sr, sc, er, ec, g):
        parents = defaultdict(tuple)

        def dijkstra(sr, sc, er, ec, g):
            open_list = [(0, sr, sc, 0)]
            heapify(open_list)
            closed_set = set()
            parents[sr, sc] = (sr, sc)

            while open_list:
                score, r, c, d = heappop(open_list)

                if (r, c) in closed_set:
                    continue
                closed_set.add((r, c))
                if (r, c) != (sr, sc):
                    parents[r, c] = (r - dirs[d][0], c - dirs[d][1], acts[d])

                if (r, c) == (er, ec):
                    return score

                for idx, (dr, dc) in enumerate(dirs):
                    nr, nc = r + dr, c + dc
                    if g[nr, nc] and g[nr, nc] != '#':
                        new_score = score + 1
                        heappush(open_list, (new_score, nr, nc, idx))
            return None

        def construct_path(parents, path, start_r, start_c, end_r, end_c):
            r, c = end_r, end_c
            while (r, c) != (start_r, start_c):
                r, c, d = parents[r, c]
                path.append(d)
            path.reverse()
            return path

        dijkstra(sr, sc, er, ec, g)
        path = construct_path(parents, [], sr, sc, er, ec)
        return path

    def find_pos(char, g):
        for k, v in g.items():
            if v == char:
                return k

    cache_dir = defaultdict(dict)
    # @cache
    def generate(s_e, ts):
        if ts <= 0:
            return ''
        if cache_dir[s_e].get(ts):
            return cache_dir[s_e][ts]

        s, e = s_e
        sr, sc = find_pos(s, g2)
        er, ec = find_pos(e, g2)
        path = find_path(sr, sc, er, ec, g2)
        path = (''.join(path)
                .replace('<v<', 'v<<')
                .replace('>^>', '>>^'))
        path += 'A'

        ans = []
        for i in range(0, len(path)):
            if i == 0:
                ans.append(generate(('A', path[0]), ts - 1))
            else:
                ans.append(generate((path[i-1], path[i]), ts - 1))

        cache_dir[s_e][ts] = path
        print('ans', ans)
        return ''.join(ans)

    total = 0
    for line in open(input_file).read().splitlines():
        ss = 'A' + line

        res0 = []
        for i in range(1, len(ss)):
            sr, sc = find_pos(ss[i-1], g)
            er, ec = find_pos(ss[i], g)

            path = find_path(sr, sc, er, ec, g)
            path = (''.join(path)
                    # .replace('^^<<', '<<^^')
                    .replace('>vv>', '>>vv')
                    .replace('>v>v', '>>vv')
                    .replace('>vvv>', '>>vvv')
                    .replace('>v>', '>>v')
                    .replace('v<v', '<vv')
                    .replace('v<<v', '<<vv')
                    .replace('v>v', '>vv')
                    .replace('v>>v', '>>vv')
                    .replace('^<^', '^^<')
                    .replace('^<<^', '^^<<')
                    .replace('<^<', '^<<')
                    .replace('<^^^<', '^^^<<')
                    .replace('<^^<', '^^<<'))

            res0.append(path + 'A')

        res0 = ['<<^^A' if x == '^^<<A' and i > 0 else x for i, x in enumerate(res0)]
        print(res0)

        times = 2
        res = []
        res0 = 'A' + ''.join(res0)
        for i in range(1, len(res0)):
            next_output = generate((res0[i-1], res0[i]), times)
            res.append(next_output)

        length = len(''.join(res))
        num = int(ss[1:4])
        print(length, num, res)
        total += length * num

    print(cache_dir)
    print(total)

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
