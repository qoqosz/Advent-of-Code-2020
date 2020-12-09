# Part 1
from itertools import combinations
from re import sub


with open('p09.txt') as f:
    numbers = [int(x) for x in f]


def validate(numbers, preamble):
    for i, n in enumerate(numbers[preamble:], preamble):
        if n not in [a + b for a, b in combinations(numbers[i - preamble:i], 2)]:
            return n


n = validate(numbers, 25)
print(n)


# Part 2
def contiguous_set(numbers, target):
    for i in range(len(numbers)):
        sum_, j = 0, i

        while sum_ < target:
            sum_ += numbers[j]
            j += 1

        if sum_ == target:
            return numbers[i:j]


subset = contiguous_set(numbers, n)
print(min(subset) + max(subset))
