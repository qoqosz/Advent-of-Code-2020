import re
from functools import lru_cache

# Part 1
bags = {}
p = re.compile(r'\d+ (.*?) bag')

with open('p07.txt') as f:
    for line in f:
        out_color, in_color = line.strip().split(' bags contain ')

        if 'no other' in in_color:
            in_color = None
        else:
            in_color = p.findall(in_color)

        bags[out_color] = in_color


@lru_cache(None)
def contains(color, target_color):
    if color == target_color:
        return True
    if bags[color] is None:
        return False
    return any(contains(c, target_color) for c in bags[color])


print(sum(contains(c, 'shiny gold') for c in bags.keys()) - 1)

# Part 2
bags = {}
p = re.compile(r'(\d+) (.*?) bag')

with open('p07.txt') as f:
    for line in f:
        out_color, in_color = line.strip().split(' bags contain ')

        if 'no other' in in_color:
            in_color = None
        else:
            in_color = p.findall(in_color)
            in_color = [(int(x[0]), x[1]) for x in in_color]

        bags[out_color] = in_color


@lru_cache(None)
def capacity(color):
    if bags[color] is None:
        return 0
    return sum(n + n * capacity(c) for n, c in bags[color])


print(capacity('shiny gold'))
