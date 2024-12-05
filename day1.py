import collections
from utils import read_integer_pairs

# --- Day 1: Historian Hysteria ---


def distance():
    # TC: O(NlogN)
    lst1, lst2 = read_integer_pairs('./input/day1.txt')

    lst1.sort()
    lst2.sort()

    return sum(map(lambda x: abs(x[1] - x[0]), zip(lst1, lst2)))

print(distance())

def similarity():
    # TC: O(N)
    lst1, lst2 = read_integer_pairs('./input/day1.txt')

    counter1 = collections.Counter(lst1)
    counter2 = collections.Counter(lst2)

    return sum(counter2[key] * key * freq for key, freq in counter1.items())

print(similarity())

