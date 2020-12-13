# Part 1
with open('p13.txt') as f:
    timestamp0 = int(f.readline())
    bus_ids = [int(x) for x in f.readline().split(',') if x != 'x']


def next_arrival(t0, bus_id):
    a, b = divmod(t0, bus_id)

    if b == 0:
        return t0
    return (a + 1) * bus_id, bus_id


next_arrivals = [next_arrival(timestamp0, bus_id)
                 for bus_id in bus_ids]
t_arrive, bus_id = min(next_arrivals, key=lambda x: x[0])
print((t_arrive - timestamp0) * bus_id)


# Part 2
from numpy import lcm

with open('p13.txt') as f:
    timestamp0 = int(f.readline())
    schedule = [(i, int(x))
                for i, x in enumerate(f.readline().split(','))
                if x != 'x']

N = len(schedule)
t0 = 100000000000000
dt = schedule[0][1]
t = t0 // dt * dt

while True:
    ids = [bus_id
           for phi, bus_id in schedule
           if (t + phi) % bus_id == 0]

    if len(ids) == N:
        print(t)
        break

    t += lcm.reduce(ids)
