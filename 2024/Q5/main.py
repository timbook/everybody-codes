from collections import deque
import numpy as np
import pandas as pd

# Part I
data = [
    deque([4, 5, 5, 3, 3]),
    deque([2, 3, 5, 3, 5]),
    deque([3, 4, 2, 2, 2]),
    deque([4, 4, 2, 4, 5])
]

def run_game(data, rnd):
    NCOL = len(data)

    active_col = rnd % NCOL
    next_col = (active_col + 1) % NCOL
    clapper = data[active_col].popleft()

    col_len = len(data[next_col])

    if clapper <= col_len:
        data[next_col].insert(clapper - 1, clapper)
    else:
        i = 2*col_len - clapper + 1
        data[next_col].insert(i, clapper)

    #  val = ''.join([str(d[0]) for d in data])
    #  print(f"{rnd+1:2}: {val}")

    return data

for rnd in range(10):
    data = run_game(data, rnd)

val = ''.join([str(d[0]) for d in data])
print(f"1 ::: {val}")

# Part II
raw = np.genfromtxt('data/everybody_codes_e2024_q05_p2.txt', dtype=int)
data = [deque(row) for row in raw.T]

counts = {}
rnd = 0
obs = []

while True:
    data = run_game(data, rnd)
    val = int(''.join([str(d[0]) for d in data]))
    
    obs.append(val)

    #  print(f"{rnd+1:2} : {val}")

    counts[val] = counts.get(val, 0) + 1

    if counts[val] >= 2024:
        break

    rnd += 1

R = rnd + 1
N = [k for k in counts.keys() if counts[k] == 2024][0]
print(f"2 ::: {R*N}")

# Part III
raw = np.genfromtxt('data/everybody_codes_e2024_q05_p3.txt', dtype=int)
data = [deque(row) for row in raw.T]

# Sample
#  data = [
    #  deque([2, 6]),
    #  deque([3, 7]),
    #  deque([4, 8]),
    #  deque([5, 9])
#  ]

#  counts = {}
#  rnd = 0
#  obs = []

#  while True:
    #  data = run_game(data, rnd)
    #  val = int(''.join([str(d[0]) for d in data]))
    
    #  obs.append(val)
    #  print(f"{rnd+1:2} : {val}")

    #  counts[val] = counts.get(val, 0) + 1

    #  if counts[val] >= 3:
        #  break

    #  rnd += 1

# Not 1008100210081004
# dn begin with 1
#  print(f"3 ::: {max(obs)}")
