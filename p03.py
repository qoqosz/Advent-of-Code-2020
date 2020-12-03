trees = 0
pos = 0
dir = 3
n = 0

# Part 1
with open('p03.txt') as f:
    for i, line in enumerate(f):
        if i == 0:
            n = len(line) - 1
        else:
            pos += dir
            char = line[pos % n]

            if char == '#':
                trees += 1

print(trees)

# Part 2
slope = []

with open('p03.txt') as f:
    for line in f:
        slope.append(list(line.strip()))


def count_trees(map, right=1, down=1):
    n = len(map[0])
    trees, pos = 0, 0

    for line in map[down::down]:
        pos += right
        char = line[pos % n]

        if char == '#':
            trees += 1

    return trees


dirs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
res = 1

for (right, down) in dirs:
    res *= count_trees(slope, right, down)

print(res)
