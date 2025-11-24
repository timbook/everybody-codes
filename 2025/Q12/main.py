import numpy as np
import networkx as nx

# PART I ================================================

raw = open('data/input1.txt', 'r').readlines()

mx = np.array([
    list(line.strip()) for line in raw
]).astype(int)
R, C = mx.shape

# Make grid
G = nx.Graph()
for r in range(R):
    for c in range(C):
        nbs = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
        nbs = [(r, c) for r, c in nbs if 0 <= r < R and 0 <= c < C]
        for r_nb, c_nb in nbs:
            G.add_edge((r, c), (r_nb, c_nb))

to_discover = [(0, 0)]
explored = set()

while to_discover:
    curr = to_discover.pop()
    explored.add(curr)
    for nb in nx.all_neighbors(G, curr):
        val_curr = mx[curr[0], curr[1]]
        val_nb = mx[nb[0], nb[1]]
        if nb not in explored and val_nb <= val_curr:
            to_discover.append(nb)

sol = len(explored)
print(f"I :: {sol}")

# PART II ================================================

raw = open('data/input2.txt', 'r').readlines()

mx = np.array([
    list(line.strip()) for line in raw
]).astype(int)
R, C = mx.shape

# Make grid
G = nx.Graph()
for r in range(R):
    for c in range(C):
        nbs = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
        nbs = [(r, c) for r, c in nbs if 0 <= r < R and 0 <= c < C]
        for r_nb, c_nb in nbs:
            G.add_edge((r, c), (r_nb, c_nb))

to_discover = [(0, 0), (R - 1, C - 1)]
explored = set()

while to_discover:
    curr = to_discover.pop()
    explored.add(curr)
    for nb in nx.all_neighbors(G, curr):
        val_curr = mx[curr[0], curr[1]]
        val_nb = mx[nb[0], nb[1]]
        if nb not in explored and val_nb <= val_curr:
            to_discover.append(nb)

sol = len(explored)
print(f"II :: {sol}")

# PART III ================================================

raw = open('data/input3.txt', 'r').readlines()

mx = np.array([
    list(line.strip()) for line in raw
]).astype(int)
R, C = mx.shape

# Make grid
G = nx.Graph()
for r in range(R):
    for c in range(C):
        nbs = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
        nbs = [(r, c) for r, c in nbs if 0 <= r < R and 0 <= c < C]
        for r_nb, c_nb in nbs:
            G.add_edge((r, c), (r_nb, c_nb))

def burn(mx, node, burnt=None):

    to_discover = [node]
    explored = set()

    while to_discover:
        curr = to_discover.pop()
        explored.add(curr)
        for nb in nx.all_neighbors(G, curr):
            val_curr = mx[curr[0], curr[1]]
            val_nb = mx[nb[0], nb[1]]
            if nb not in explored and val_nb <= val_curr:
                to_discover.append(nb)

    return explored if not burnt else explored - burnt

# Node 1: Greedily find optimal node
node1 = max(G.nodes, key=lambda n: len(burn(mx, n)))
burnt1 = burn(mx, node1)
print(f"Picked {node1} first")

# Node 2: Find best node after 1st finishes
node2 = max(G.nodes, key=lambda n: len(burn(mx, n, burnt1)))
burnt2 = burn(mx, node2) | burnt1
print(f"Picked {node2} second")

# Node 3: Find best node after 1st and 2nd finishes
node3 = max(G.nodes, key=lambda n: len(burn(mx, n, burnt1 | burnt2)))
burnt3 = burn(mx, node3) | burnt1 | burnt2
print(f"Picked {node3} third")

sol = len(burnt1 | burnt2 | burnt3)
print(f"III :: {sol}")
