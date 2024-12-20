import time
from functools import cache

start_time = time.time()

day = 19
is_test = False
input_file = f'./input/day{day}{"_test" if is_test else ""}.txt'

def sol():
    p1, p2 = open(input_file, 'r').read().split('\n\n')
    p1 = p1.split(', ')
    test_words = p2.split('\n')

    word_dicts = set(p1)

    # TODO: dp

    @cache
    def dfs(i, s):
        if i == 0:
            return True

        for w in word_dicts:
            length = len(w)

            if s[i - length: i] == w and dfs(i - length, s):
                return True
        return False

    total = 0
    for word in test_words:
        if dfs(len(word), word):
            # print('word', word)
            total += 1

    print(total)


sol()
print(f'{(time.time() - start_time) * 1000:.3f}ms')
