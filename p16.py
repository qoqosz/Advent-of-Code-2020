# Part 1
import re
import pandas as pd
from collections import defaultdict


rng = re.compile(r'(\d+)-(\d+)')
ranges = defaultdict(set)

with open('p16.txt') as f:
    for i, line in enumerate(f):
        if i < 20:
            rngs = [[*map(int, x)] for x in rng.findall(line)]
            for r in rngs:
                ranges[i].update(set(range(r[0], r[1] + 1)))
        if i == 22:
            my_ticket = [int(x) for x in line.strip().split(',')]

df = pd.read_csv('p16.txt', skiprows=25, header=None)
is_valid = df.applymap(lambda x: any(x in rng for rng in ranges.values()))
print('%d' % df[~is_valid].sum().sum())

# Part 2
df = df.loc[is_valid.all(axis=1)]

res, columns = 1, set(range(20))

candidates = [df.applymap(lambda x: x in rng).all(axis=0)
              for rng in ranges.values()]
candidates = [(field_id, x[x].index.tolist())
              for field_id, x in enumerate(candidates)]
candidates.sort(key=lambda x: len(x[1]))

used_cols = set()
mapping = {}

for field_id, col_ids in candidates:
    col = set(col_ids) - used_cols
    used_cols.update(col)
    mapping[field_id] = col.pop()

res = 1
for i in range(6):
    res *= my_ticket[mapping[i]]

print(res)
