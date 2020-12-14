import re
from itertools import product

# Part 1
turn_on = lambda x, i: x | 1 << i
turn_off = lambda x, i: x & ~(1 << i)
switch = {'0': turn_off, '1': turn_on}
mem, mask = {}, ''

def apply_mask(val, mask):
    for code, pos in mask:
        val = switch[code](val, pos)

    return val

with open('p14.txt') as f:
    for line in f:
        line = line.strip()

        if line.startswith('mask'):
            mask = [(x, i)
                    for i, x in enumerate(reversed(line[7:]))
                    if x in "01"]
        else:
            m = re.search(r'mem\[(\d+)\] = (\d+)', line)
            key, val = map(int, m.groups())
            mem[key] = apply_mask(val, mask)

print(sum(mem.values()))

# Part 2
def apply_floating_mask(val, mask):
    # val = 0
    # 1. apply a mask where not X
    # 2. iterate prod of possible masks to get new nums
    for code, pos in mask:
        if code in ['1']:
            val = switch[code](val, pos)

    res = []
    idx = [x[1] for x in mask if x[0] == 'X']

    for comb in product('01', repeat=len(idx)):
        for bit, pos in zip(comb, idx):
            val = switch[bit](val, pos)

        res.append(val)
    return res

mem, mask = {}, ''

with open('p14.txt') as f:
    for line in f:
        line = line.strip()

        if line.startswith('mask'):
            mask = [(x, i) for i, x in enumerate(reversed(line[7:]))]
        else:
            m = re.search(r'mem\[(\d+)\] = (\d+)', line)
            key, val = map(int, m.groups())
            addrs = apply_floating_mask(key, mask)
            for addr in addrs:
                mem[addr] = val

print(sum(mem.values()))
