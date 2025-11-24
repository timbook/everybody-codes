import numpy as np
from itertools import permutations


def get_all_moves(locs):
    moves = [
        (2, 1), (2, -1), (-2, -1), (-2, 1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    locs_new = []
    for loc in locs:
        for r_move, c_move in moves:
            loc_new = (loc[0] + r_move, loc[1] + c_move)
            locs_new.append(loc_new)

    return locs_new

def sheep_move(locs):
    return [(r + 1, c) for r, c in locs]

def sweep_edges(locs, R, C):
    return [
        (r, c) for r, c in locs
        if 0 <= r < R and 0 <= c < C
    ]

def dedup(locs):
    return list(set(locs))

def eat_sheep(sheep, dragons, zones):
    n_sheep = len(sheep)
    eaten = set(sheep) & set(dragons) - zones
    sheep = set(sheep) - eaten
    return sheep, n_sheep - len(sheep)

# PART I ==============================================

# raw = open('data/sample1.txt', 'r').readlines()
raw = open('data/input1.txt', 'r').readlines()
mx = np.array([list(line.strip()) for line in raw])

R, C = mx.shape

rd, cd = np.where(mx == 'D')
rd, cd = rd[0], cd[0]

rs, cs = np.where(mx == 'S')
sheep = [(r, c) for r, c in zip(rs, cs)]
locs_possible = [(rd, cd)]
prev_locs = locs_possible.copy()
for _ in range(4):
    prev_locs = get_all_moves(prev_locs)
    locs_possible.extend(prev_locs)

locs_possible = [
    (r, c) for r, c in locs_possible
    if 0 <= r < R and 0 <= c < C
]

sol = len(set(sheep) & set(locs_possible))
print(f"I :: {sol}")

# PART II =============================================

# raw = open('data/sample2.txt', 'r').readlines()
raw = open('data/input2.txt', 'r').readlines()
mx = np.array([list(line.strip()) for line in raw])

R, C = mx.shape

rd, cd = np.where(mx == 'D')
dragons = [(rd[0], cd[0])]

rs, cs = np.where(mx == 'S')
sheep = [(r, c) for r, c in zip(rs, cs)]
n_sheep_init = len(sheep)

rz, cz = np.where(mx == '#')
zones = {(r, c) for r, c in zip(rz, cz)}

sheep_eaten = 0
for i in range(20):
    # dragon moves
    dragons = dedup(get_all_moves(dragons))
    # sweep board
    dragons = sweep_edges(dragons, R, C)
    # eat sheep
    sheep, ate = eat_sheep(sheep, dragons, zones)
    sheep_eaten += ate

    # sheep moves
    sheep = sheep_move(sheep)
    # sweep board
    sheep = sweep_edges(sheep, R, C)
    # eat sheep
    sheep, ate = eat_sheep(sheep, dragons, zones)
    sheep_eaten += ate

sol = sheep_eaten
print(f"II :: {sol}")
