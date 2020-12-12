# Part 1
with open('p12.txt') as f:
    steps = [x.strip() for x in f]

direction = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
direction_inv = {v: k for k, v in direction.items()}
coords = {'E': [1, 0], 'N': [0, 1], 'W': [-1, 0], 'S': [0, -1]}


def turn(orientation, instruction):
    sign = 1 if instruction[0] == 'L' else -1
    rotate_by = int(instruction[1:])
    delta = sign * rotate_by

    return direction[(direction_inv[orientation] + delta) % 360]


def move(pos, action):
    direction = action[0]

    if direction == 'F':
        direction = orientation

    direction = coords[direction]
    move_by = int(action[1:])

    return [x + move_by * y for x, y in zip(pos, direction)]


orientation = 'E'
pos = [0, 0]


for step in steps:
    cmd = step[0]

    if cmd in ['L', 'R']:
        orientation = turn(orientation, step)
    else:
        pos = move(pos, step)

print(sum(map(abs, pos)))


# Part 2
def move_ship(pos, action, waypoint):
    move_by = int(action[1:])

    for i in range(move_by):
        pos = [x + y for x, y in zip(pos, waypoint)]

    return pos


def move_waypoint(step, waypoint):
    return move(waypoint, step)


def turn_waypoint(orientation, step):
    # 90 -> (x, y) -> (-y, x)
    # 180 -> (x, y) -> (-x, -y)
    # 270 -> (x, y) -> (y, -x)
    sign = 1 if step[0] == 'L' else -1
    rotate_by = int(step[1:])
    delta = (sign * rotate_by) % 360

    if delta == 90:
        return [-orientation[1], orientation[0]]
    elif delta == 180:
        return [-orientation[0], -orientation[1]]
    elif delta == 270:
        return [orientation[1], -orientation[0]]
    else:
        return orientation


waypoint = [10, 1]
pos = [0, 0]

for step in steps:
    cmd = step[0]

    if cmd == 'F':
        pos = move_ship(pos, step, waypoint)
    elif cmd in ['L', 'R']:
        waypoint = turn_waypoint(waypoint, step)
    else:
        waypoint = move_waypoint(step, waypoint)

print(sum(map(abs, pos)))
