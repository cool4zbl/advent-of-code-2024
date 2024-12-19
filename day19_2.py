import time
from collections import defaultdict
from functools import cache

start_time = time.time()

day = 19
is_test = False
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def sol():
    p1, p2 = open(input_file, 'r').read().split('\n\n')
    p1 = p1.split(', ')
    test_words = p2.split('\n')

    word_dict = set(p1)

    pattern_count = defaultdict(int)

    @cache
    def dfs(s):
        if s == '':
            return 1
        if pattern_count[s]:
            return pattern_count[s]

        matched_pattern = [w for w in word_dict if s.startswith(w)]

        for matched in matched_pattern:
            pattern_count[s] += dfs(s[len(matched):])

        return pattern_count[s]

    total = 0
    for word in test_words:
        count = dfs(word)
        total += count

    print(total)

    # root = TrieNode()
    # for word in word_dict:
    #     cur = root
    #     for c in word:
    #         if c not in cur.children:
    #             cur.children[c] = TrieNode()
    #         cur = cur.children[c]
    #     cur.is_word = True
    #
    # ways = defaultdict(list)
    # for s in found_words:
    #     dp = [False] * len(s)
    #     way = []
    #     i = 0
    #     while i < len(s):
    #         cur = root
    #         j = i
    #         while j < len(s):
    #             c = s[j]
    #             if c not in cur.children:
    #                 break
    #             cur = cur.children[c]
    #             if cur.is_word:
    #                 way.append(s[i:j+1])
    #             j += 1
    #         i = j
    #     ways[s].append(way)

sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
