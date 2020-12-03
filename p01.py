import random
from functools import reduce
from operator import mul


def problem(k=2):
    with open('p01.txt') as f:
        data = [int(line) for line in f]

    while True:
        sample = random.choices(data, k=k)

        if sum(sample) == 2020:
            return reduce(mul, sample, 1)


if __name__ == '__main__':
    print('Part 1:', problem(2))
    print('Part 2:', problem(3))
