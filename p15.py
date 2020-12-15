from collections import defaultdict
from itertools import islice
# Part 1
starting_nums = '9,19,1,6,0,5,4'
starting_nums = [*map(int, starting_nums.split(','))]


def play(starting_nums):
    yield 0
    n_start = len(starting_nums)
    history = defaultdict(list)
    turn, val = 1, 0

    while True:
        if turn <= n_start:
            val = starting_nums[turn - 1]
        else:
            if len(history[val]) <= 1:
                val = 0
            else:
                val = history[val][-1] - history[val][-2]

        history[val].append(turn)
        turn += 1
        yield val


print(next(islice(play(starting_nums), 2020, None)))

# Part 2
print(next(islice(play(starting_nums), 30000000, None)))
