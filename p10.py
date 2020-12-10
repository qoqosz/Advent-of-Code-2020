from collections import Counter
from itertools import groupby
from functools import lru_cache
from math import prod

# Part 1
with open('p10.txt') as f:
    adapters = [int(x) for x in f]

adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()
diffs = [y - x for x, y in zip(adapters, adapters[1:])]
diff_count = Counter(diffs)
print(diff_count[1] * diff_count[3])


# Part 2
# Elements where diff in jolts is < 3 can be rearranged.
# Number of this rearrangement is based only on a total jolts diff.
# E.g.
#   - diff 2 jolts yields: (1, 1), (2) - 2 arrangements
#   - diff 3 jolts yields: (1, 1, 1), (1, 2), (2, 1), (3) - 4 arrangements, etc.
shuffle_groups = [sum(group)
                  for k, group
                  in groupby(diffs[:-1], lambda x: x == 3)
                  if not k]


# Number of diff arrangements depends on n-th Fibonnaci number
@lru_cache(None)
def fib(x):
    return x if x < 3 else fib(x - 1) + fib(x - 2)


print(prod(fib(x + 1) - 1 for x in shuffle_groups))
