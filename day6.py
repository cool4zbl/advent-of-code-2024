import re
from collections import deque, defaultdict

is_test = False
day = 6

def sol():
    with open(f'./input/day{day}{'_test' if is_test else ''}.txt', 'r') as file:
        pass