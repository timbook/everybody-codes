from itertools import pairwise, combinations

def is_opp(a, b, N):
    return abs(a - b) == N // 2

def count_crosses(a, b, crosses):
    m = min(a, b)
    M = max(a, b)
    cross_count = 0
    for pair, count in crosses.items():
        l, r = pair
        cross_cond1 = m < l < M and (r < m or r > M)
        cross_cond2 = m < r < M and (l < m or l > M)
        if cross_cond1 or cross_cond2:
            cross_count += count
    return cross_count

# PART I ======================================

raw = open('data/input1.txt', 'r').read()
data = [int(i) for i in raw.strip().split(',')]
N = 32

count = sum(is_opp(a, b, N) for a, b in pairwise(data))
print(f"I :: {count}")

# PART II =====================================

raw = open('data/input2.txt', 'r').read()
data = [int(i) for i in raw.strip().split(',')]
N = 256

crosses = {}
knots = 0
for a, b in pairwise(data):
    knots += count_crosses(a, b, crosses)
    crosses[(a, b)] = crosses.get((a, b), 0) + 1

print(f"II :: {knots}")

# PART III ====================================

raw = open('data/input3.txt', 'r').read()
data = [int(i) for i in raw.strip().split(',')]
N = 256

crosses = {}
for a, b in pairwise(data):
    crosses[(a, b)] = crosses.get((a, b), 0) + 1

best = 0
for a, b in combinations(range(1, N + 1), 2):

    knots = count_crosses(a, b, crosses) \
        + crosses.get((a, b), 0) \
        + crosses.get((b, a), 0)

    best = knots if knots > best else best

print(f"III :: {best}")
