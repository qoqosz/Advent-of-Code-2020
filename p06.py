from functools import reduce
from operator import and_


# Part 1
count = 0

with open('p06.txt') as f:
    answers = set()

    for line in f:
        line = line.strip()

        if not line:
            count += len(answers)
            answers = set()
        else:
            answers.update(line)

count += len(answers)
print(count)

# Part 2
count = 0

with open('p06.txt') as f:
    answers = []

    for line in f:
        line = line.strip()

        if not line:
            count += len(reduce(and_, answers))
            answers = []
        else:
            answers.append(set(line))

count += len(reduce(and_, answers))
print(count)
