# Part 1
prog, acc, i = [], 0, 0

with open('p08.txt') as f:
    for line in f:
        cmd, val = line.strip().split(' ')
        val = int(val)
        prog.append((cmd, val))

executed = [False] * len(prog)


while True:
    if executed[i]:
        print(acc)
        break

    executed[i] = True

    cmd, val = prog[i]

    if cmd == 'acc':
        acc, i = acc + val, i + 1
    elif cmd == 'jmp':
        i += val
    else:
        i += 1


# Part 2
def exe(prog):
    acc, i, executed = 0, 0, [False] * len(prog)

    while True:
        try:
            if executed[i]:
                return False, acc
        except IndexError:
            return True, acc

        executed[i] = True
        cmd, val = prog[i]

        if cmd == 'acc':
            acc, i = acc + val, i + 1
        elif cmd == 'jmp':
            i += val
        else:
            i += 1


for i, (cmd, val) in enumerate(prog):
    if cmd in ['nop', 'jmp']:
        new_prog = list(prog)
        new_prog[i] = ({'nop': 'jmp', 'jmp': 'nop'}[cmd], val)

        exe_code, acc = exe(new_prog)

        if exe_code:
            print(acc)
            break
