# Part 1
def seat_id(code):
    row = int(code[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(code[-3:].replace('R', '1').replace('L', '0'), 2)

    return row * 8 + col


with open('p05.txt') as f:
    ids = [seat_id(line.strip()) for line in f]

print(max(ids))

# Part 2
all_ids = list(range(min(ids), max(ids) + 1))
print(set(all_ids) - set(ids))
