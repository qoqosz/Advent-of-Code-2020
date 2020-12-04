# Part 1
fields = set(['byr', 'iyr', 'eyr', 'hgt',
              'hcl', 'ecl', 'pid', 'cid'])
passports = []

with open('p04.txt') as f:
    data = {}
    for line in f:
        line = line.strip()

        if not line:
            if data:
                passports.append(data)
            data = {}
        else:
            data.update({k: v
                         for k, v
                         in map(lambda x: x.split(':'),
                                line.split(' '))})

passports.append(data)


def is_valid(passport):
    keys = set(passport.keys())

    if keys == fields:
        return True
    if len(keys) == 7:
        return fields - keys == {'cid'}

    return False


print(sum(map(is_valid, passports)))

# Part 2
hex_chars = [str(x) for x in range(10)]
hex_chars += ['a', 'b', 'c', 'd', 'e', 'f']


def is_valid_two(passport):
    if not is_valid(passport):
        return False

    keys = set(passport.keys())
    # validation
    byr = int(passport['byr']) in range(1920, 2002 + 1)
    iyr = int(passport['iyr']) in range(2010, 2020 + 1)
    eyr = int(passport['eyr']) in range(2020, 2030 + 1)
    hgt_unit = passport['hgt'][-2:]

    if hgt_unit in ['in', 'cm']:
        if hgt_unit == 'in':
            hgt = int(passport['hgt'][:-2]) in range(59, 76 + 1)
        else:
            hgt = int(passport['hgt'][:-2]) in range(150, 193 + 1)
    else:
        hgt = False

    hcl = ((passport['hcl'][0] == '#')
           and
           (len(passport['hcl'][1:]) == 6)
           and
           all(x in hex_chars for x in passport['hcl'][1:]))
    ecl = passport['ecl'] in ['amb', 'blu', 'brn', 'gry',
                              'grn', 'hzl', 'oth']
    pid = (all(x.isdigit() for x in passport['pid'])
           and
           (len(passport['pid']) == 9))

    return all([byr, iyr, eyr, hgt, hcl, ecl, pid])


print(sum(map(is_valid_two, passports)))
