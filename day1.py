import collections
from utils import read_integer_pairs

# --- Day 1: Historian Hysteria ---


def distance():
    lst1, lst2 = read_integer_pairs('./day1.txt')

    lst1.sort()
    lst2.sort()

    return sum(map(lambda x: abs(x[1] - x[0]), zip(lst1, lst2)))

print(distance())

def similarity():
    lst1, lst2 = read_integer_pairs('./day1.txt')

    counter1 = collections.Counter(lst1)
    counter2 = collections.Counter(lst2)

    return sum(counter2[key] * key * freq for key, freq in counter1.items())

print(similarity())

