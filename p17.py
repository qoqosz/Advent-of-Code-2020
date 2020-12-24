# Part 1
from itertools import product

space = {}

with open('p17.txt') as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == '#':
                space[(i, j, 0)] = c


def get_neighbours(p):
    x, y, z = p
    for dx, dy, dz in product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]):
        if dx == dy == dz == 0:
            continue
        yield (x + dx, y + dy, z + dz)


def n_neighbours(p):
    return sum(space.get(n, '.') == '#'
               for n in get_neighbours(p))


def check(p, space, updates):
    n = n_neighbours(p)

    if space.get(p, '.') == '#' and n not in [2, 3]:
        updates[p] = '.'
    elif n == 3:
        updates[p] = '#'


def cycle(space):
    updates, visited = {}, set()

    for p in space:
        check(p, space, updates)

        for n in get_neighbours(p):
            if n not in visited:
                check(n, space, updates)
                visited.update([n])

    space.update(updates)


for i in range(6):
    cycle(space)

print(list(space.values()).count('#'))

# Part 2
space = {}

with open('p17.txt') as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == '#':
                space[(i, j, 0, 0)] = c


def get_neighbours(p):
    x, y, z, w = p
    for dx, dy, dz, dw in product([-1, 0, 1], [-1, 0, 1],
                                  [-1, 0, 1], [-1, 0, 1]):
        if dx == dy == dz == dw == 0:
            continue
        yield (x + dx, y + dy, z + dz, w + dw)


for i in range(6):
    cycle(space)


print(list(space.values()).count('#'))
