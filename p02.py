from collections import Counter

p1_count, p2_count = 0, 0

with open('p02.txt') as f:
    for line in f:
        rng, char, text = line.split(' ')
        min_, max_ = map(int, rng.split('-'))
        char = char.strip(':')
        counter = Counter(text)

        if min_ <= counter[char] <= max_:
            p1_count += 1

        if (char == text[min_ - 1]) ^ (char == text[max_ - 1]):
            p2_count += 1

print('Part 1:', p1_count)
print('Part 2:', p2_count)
