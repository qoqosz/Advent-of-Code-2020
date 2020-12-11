import numpy as np


# Part 1
with open('p11.txt') as f:
    data = np.array([list(x.strip()) for x in f])

shifts = [(1, 0), (-1, 0), (0, 1), (0, -1),
          (1, 1), (1, -1), (-1, 1), (-1, -1)]


def __repr__(data):
    return '\n'.join([''.join(map(str, line)) for line in data])


np.set_string_function(__repr__)


def shift(data, dx, dy, fill='.'):
    """Shift array in (dx, dy) direction."""
    data = np.roll(data, dx, axis=1)
    if dx < 0:
        data[:, dx:] = fill
    elif dx > 0:
        data[:, :dx] = fill

    data = np.roll(data, dy, axis=0)
    if dy < 0:
        data[dy:, :] = fill
    elif dy > 0:
        data[:dy, :] = fill

    return data


def n_neighbours(data, shifts, neighbour='L'):
    """Count neighbours of any eat (L) on a grid."""
    mask = data != '.'
    stacked = np.stack([shift(data, dx, dy) for dx, dy in shifts], axis=0)
    count = (stacked == neighbour).sum(axis=0)

    return np.where(mask, count, 0)


def occupy(data, shifts):
    """Run one iteration (2 rounds) of the algorithm."""
    data = data.copy()
    # Round 1
    is_empty = data == 'L'
    is_adj_empty = n_neighbours(data, shifts, '#') == 0

    data[is_empty & is_adj_empty] = '#'

    # Round 2
    is_occupied = data == '#'
    is_adj_occupied = n_neighbours(data, shifts, '#') >= 4
    data[is_occupied & is_adj_occupied] = 'L'

    return data


while True:
    new_data = occupy(data, shifts)

    if (new_data == data).all():
        print(np.sum(new_data == '#'))
        break

    data = new_data


# Part 2
with open('p11.txt') as f:
    data = np.array([list(x.strip()) for x in f])


def is_occupied(data, pos, dir_):
    x, y = pos
    res = []

    while True:
        try:
            x, y = x + dir_[0], y + dir_[1]

            if x < 0 or y < 0:
                raise IndexError

            val = data[x, y]
            res.append(val)
        except IndexError:
            res = [x for x in res if x != '.']

            if not res:
                return False
            return res[0] == '#'


def n_occupied(data, dirs):
    res = np.zeros(data.shape, dtype=int)

    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            res[i, j] = sum(is_occupied(data, (i, j), dir_)
                            for dir_ in dirs)

    return res


def occupy2(data, dirs):
    data = data.copy()
    # Round 1
    is_empty = data == 'L'
    is_visible_empty = n_occupied(data, dirs) == 0
    data[is_empty & is_visible_empty] = '#'

    # Round 2
    is_occupied = data == '#'
    is_vis_occupied = n_occupied(data, dirs) >= 5
    data[is_occupied & is_vis_occupied] = 'L'

    return data


while True:
    new_data = occupy2(data, shifts)

    if (new_data == data).all():
        print(np.sum(new_data == '#'))
        break

    data = new_data
