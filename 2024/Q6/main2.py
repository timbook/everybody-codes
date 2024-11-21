import networkx as nx

# Part I

lines = open('data/everybody_codes_e2024_q06_p1.txt', 'r').readlines()

class Node:
    def __init__(self, line):
        name, children = line.strip().split(':')
        self.name = name
        self.children = children.split(',')

    def __repr__(self):
        return f"Node({self.name}) -> {' '.join(self.children)}"

    def explore(self, chain=[]):
        for child in self.children:
            if child == '@':
                paths.append(chain + [self.name, '@'])
            elif child not in nodes:
                paths.append(chain + [child])
            else:
                nodes[child].explore(chain=chain + [self.name])


nodes_list = [Node(line) for line in lines]
nodes = {n.name : n for n in nodes_list}

paths = []
nodes['RR'].explore()
lens = [len(p) for p in paths]

counts = {}
for l in lens:
    counts[l] = counts.get(l, 0) + 1

uniq_len = [k for k, v in counts.items() if v == 1][0]
best_path = [p for p in paths if len(p) == uniq_len][0]
sol = ''.join(best_path)
print(f"A ::: {sol}")

# Part II

lines = open('data/everybody_codes_e2024_q06_p2.txt', 'r').readlines()

nodes_list = [Node(line) for line in lines]
nodes = {n.name : n for n in nodes_list}

paths = []
nodes['RR'].explore()
lens = [len(p) for p in paths]

counts = {}
for l in lens:
    counts[l] = counts.get(l, 0) + 1

uniq_len = [k for k, v in counts.items() if v == 1][0]
best_path = [p for p in paths if len(p) == uniq_len][0]
sol = ''.join([n[0] for n in best_path])

print(f"B ::: {sol}")

# Part III

#  lines = open('data/everybody_codes_e2024_q06_p3.txt', 'r').readlines()

#  nodes_list = [Node(line) for line in lines]
#  nodes = {n.name : n for n in nodes_list}

#  paths = []
#  nodes['RR'].explore()
