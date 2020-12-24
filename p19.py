# Part 1
import re

rules = {}

with open('p19.txt') as f:
    doc = f.read()
    patterns, words = doc.split('\n\n')

    for pattern in patterns.split('\n'):
        m = re.findall(r'[\dab|]+', pattern)
        rules[m[0]] = m[1:]

words = words.split('\n')


def pattern(n):
    if n == '|':
        return n

    r = rules[n]

    if r[0].isalpha():
        return r[0]

    return '(?:%s)' % ''.join(map(pattern, r))


print(sum(1 for w in words if re.fullmatch(pattern('0'), w)))


# Part 2
def pattern2(n):
    if n == '|':
        return n
    if n == '8':
        # re '+' num of group 42
        return '(?:%s)+' % pattern2('42')
    if n == '11':
        # 11 == (42)..(42)(31)..(31)
        # where there's the same num of these groups (42) and (31)
        # so: (42 11) | (42 42 11 11) | (42 42 42 11 11 11) | ...
        return '(?:%s)' % '|'.join(pattern2('42') * i + pattern2('31') * i for i in range(1, 20))

    r = rules[n]

    if r[0].isalpha():
        return r[0]

    return '(?:%s)' % ''.join(map(pattern2, r))


print(sum(1 for w in words if re.fullmatch(pattern2('0'), w)))
