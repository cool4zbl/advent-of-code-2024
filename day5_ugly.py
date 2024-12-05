import time
from collections import defaultdict

# --- Day 5: Print Queue ---

start_time = time.time()

is_test = False
day = 5


def sol():
    preq = []
    pages = []
    with open(f'./input/day{day}{'_test' if is_test else ''}.txt', 'r') as file:
        str = file.read()
        p1, p2 = str.split('\n\n')

        for line in p1.split('\n'):
            n1, n2 = line.split('|')
            preq.append([int(n1), int(n2)])


        p2s = p2.split('\n')

        for line in p2s:
            ps = [int(x) for x in line.split(',')]
            pages.append(ps)

    n = 100
    adjList = [[] for _ in range(n)]

    for pre, after in preq:
        adjList[pre].append(after)

    res = []
    un_res = []
    for ps in pages:
        ok = True
        r_ps = ps[::-1]
        for i, page in enumerate(r_ps):
            for rely in adjList[page]:
                if rely in r_ps[i+1:]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            res.append(ps)
        else:
            un_res.append(ps)

    total = 0
    for ps in res:
        total += ps[len(ps) // 2]

    end1 = time.time()
    print(f'p1 = {total}, time = {end1 - start_time:.6f} seconds')

    deps = [[] for _ in range(n)]
    for pre, after in preq:
        deps[after].append(pre)

    total = 0
    for ps in un_res:
        indegree = defaultdict(list)
        for p in ps:
            for d in adjList[p]:
                if d in ps and d not in indegree[p]:
                    indegree[p].append(d)

        n = len(ps)
        for key, values in indegree.items():
            if len(values) == n // 2:
                total += key

    print(f'p2 = {total}, time = {time.time() - end1:.6f} seconds')

sol()





