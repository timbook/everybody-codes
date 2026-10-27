from itertools import pairwise

raw = open('data/input1.txt', 'r').read().strip()
data = [int(n) for n in raw.split(',')]

def n_to_need(n):
    if int(n**0.5) == n**0.5:
        return 0
    else:
        lowest_sq = int(n**0.5)
        return (lowest_sq + 1)**2 - n

n_needed = [n_to_need(n) for n in data]
sol = sum(n_needed)
print(f"A ::: {sol}")

# ====================================================

raw = open('data/input2.txt', 'r').read().strip()
data = [int(n) for n in raw.split(',')]

def get_n_needed(n):
    if n <= 8:
        return 8 - n
    else:
        return {0: 0, 1: 3, 2: 2, 3: 1}[n % 4]

n_needed = [get_n_needed(n) for n in data]
sol = sum(n_needed)
print(f"B ::: {sol}")

# ====================================================

raw = open('data/input3.txt', 'r').read().strip()
data = [int(n) for n in raw.split(',')]

# Build list
n = 3
M = max(data)
bounds = [0]
while n**2 - 1 < M:
    bounds.append(n**2 - 1)
    n += 2
bounds.append(n**2 - 1)

def get_n_needed(n):
    for lb, ub in pairwise(bounds):
        if lb < n <= ub:
            return ub - n

n_needed = [get_n_needed(n) for n in data]
sol = sum(n_needed)
print(f"C ::: {sol}")
