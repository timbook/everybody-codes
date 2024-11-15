import networkx as nx

lines = open('data/everybody_codes_e2024_q06_p1.txt', 'r').readlines()

#  lines = """
#  RR:A,B,C
#  A:D,E
#  B:F,@
#  C:G,H
#  D:@
#  E:@
#  F:@
#  G:@
#  H:@
#  """.strip().split('\n')

n_fruit = 0

for i, line in enumerate(lines):
    if '@' in line:
        n_fruit += 1
        lines[i] = line.replace('@', '@' + str(n_fruit))

g = nx.Graph()

for line in lines:
    parent, rhs = line.strip().split(':')
    children = rhs.split(',')

    # Nodes
    g.add_node(parent)
    for child in children:
        if child not in g:
            g.add_node(child)

    # Edges
    for child in children:
        g.add_edge(parent, child)

path_lens = []
for i in range(1, n_fruit + 1):
    target = f"@{i}"
    L = nx.shortest_path(g, 'RR', target)
    path_lens.append(L)

sol = ''.join(min(path_lens, key=len))

# Not RRBHMD@
# Not RRSWDB@
print(f"1 ::: {sol}")
    
