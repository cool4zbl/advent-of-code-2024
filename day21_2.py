from collections import defaultdict
import time
from functools import cache
from heapq import heapify, heappop, heappush
from itertools import permutations

start_time = time.time()

is_test = False
day = 21
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

origin_dirs = ((0, 1, '>'), (-1, 0, '^'), (1, 0, 'v'), (0, -1, '<'))
dirss = list(permutations(origin_dirs, 4))

def build_grid(ls):
    return defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}, len(ls), len(ls[0])

def sol():
    g, m, n = build_grid([list('789'), list('456'), list('123'), list('#0A')])
    g2, _, _ = build_grid([list('#^A'), list('<v>')])

    def find_path(sr, sc, er, ec, g, dirs):
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
                    parents[r, c] = (r - dirs[d][0], c - dirs[d][1], dirs[d][2])

                if (r, c) == (er, ec):
                    return score

                for idx, (dr, dc, _) in enumerate(dirs):
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

    @cache
    def find_short_path(s, e, dirs):
        sr, sc = find_pos(s, g2)
        er, ec = find_pos(e, g2)
        p = find_path(sr, sc, er, ec, g2, dirs)

        p = (''.join(p)
             .replace('<v<', 'v<<')
             .replace('>^>', '>>^'))
        p += 'A'
        return p

    def pairs_from_path(path, prefix='A'):
        if not path:
            return []
        pairs = [(prefix, path[0])]
        pairs.extend((path[i - 1], path[i]) for i in range(1, len(path)))
        return pairs

    @cache
    def get_dir(path, dep, dirs):
        if dep == 0:
            ps = pairs_from_path(path, prefix='A')
            return ''.join(find_short_path(s, e, dirs) for s, e in ps)

        subpaths = []
        if path:
            subpaths.append('A' + path[0])
            for i in range(1, len(path)):
                subpaths.append(path[i-1] + path[i])
        return ''.join(get_dir(sp, dep - 1, dirs) for sp in subpaths)

    @cache
    def generate(path_str, ts, dirs):
        if ts <= 0:
            return len(path_str)

        t = 0
        for p in path_str.rstrip('A').split('A'):
            t += generate(get_dir(p + 'A', 0, dirs), ts - 1, dirs)
        return t

    total = 0
    for line in open(input_file).read().splitlines():
        ss = 'A' + line

        res_digit = []
        # digit pad
        for i in range(1, len(ss)):
            sr, sc = find_pos(ss[i-1], g)
            er, ec = find_pos(ss[i], g)

            path = find_path(sr, sc, er, ec, g, origin_dirs)
            path = (''.join(path)
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

            res_digit.append(path + 'A')

        print(res_digit)

        times = 25
        for choice in res_digit:
            length = min(generate(choice, times, dirs) for dirs in dirss)
            # so lucky
            # length = generate(choice, times, origin_dirs)
            num = int(ss[1:4])
            print(length, num)
            total += length * num

    # 218309335714068
    print(total)

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
