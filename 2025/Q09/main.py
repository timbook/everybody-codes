import numpy as np
import networkx as nx
from itertools import combinations

def find_child(seqs):
    child_candidates = []
    for i in range(3):
        ch = seqs[i]
        p1 = seqs[(i + 1) % 3]
        p2 = seqs[(i + 2) % 3]
        can_child = all([a == b or a == c for a, b, c in zip(ch, p1, p2)])
        child_candidates.append(can_child)

    child_ix = child_candidates.index(True)
    ch = np.array(list(seqs[child_ix]))
    p1 = np.array(list(seqs[(child_ix + 1) % 3]))
    p2 = np.array(list(seqs[(child_ix + 2) % 3]))
    return ch, p1, p2

def is_child(ch, p1, p2):
    for a, b, c in zip(ch, p1, p2):
        if a != b and a != c:
            return False
    return True

def score_family(ch, p1, p2):
    ch = np.array(list(ch))
    p1 = np.array(list(p1))
    p2 = np.array(list(p2))
    return np.sum(ch == p1) * np.sum(ch == p2)


# PART I =========================================

# raw = open('data/sample1.txt', 'r').readlines()
raw = open('data/input1.txt', 'r').readlines()

seqs = [seq.strip().split(':')[1] for seq in raw]

ch, p1, p2 = find_child(seqs)

sim1 = np.sum(ch == p1)
sim2 = np.sum(ch == p2)
sol = sim1 * sim2

print(f"I :: {sol}")

# PART II ========================================

# raw = open('data/sample2.txt', 'r').readlines()
raw = open('data/input2.txt', 'r').readlines()

seqs = [seq.strip().split(':')[1] for seq in raw]
L = len(seqs)

children = []
for i, j in combinations(range(L), 2):
    p1, p2 = seqs[i], seqs[j]
    for k in range(L):
        if k == i or k == j:
            continue
        ch = seqs[k]
        if is_child(ch, p1, p2):
            children.append((k, i, j))

score = 0
for i, j, k in children:
    ch = seqs[i]
    p1 = seqs[j]
    p2 = seqs[k]

    score += score_family(ch, p1, p2)

print(f"II :: {score}")

# PART III =======================================

# raw = open('data/sample3a.txt', 'r').readlines()
raw = open('data/input3.txt', 'r').readlines()

seqs = [seq.strip().split(':')[1] for seq in raw]
L = len(seqs)

children = []
for i, j in combinations(range(L), 2):
    p1, p2 = seqs[i], seqs[j]
    for k in range(L):
        if k == i or k == j:
            continue
        ch = seqs[k]
        if is_child(ch, p1, p2):
            children.append((k + 1, i + 1, j + 1))

G = nx.Graph()
for ch, p1, p2 in children:
    G.add_edge(ch, p1)
    G.add_edge(ch, p2)

sol = sum(max(nx.connected_components(G), key=len))
print(f"III :: {sol}")
