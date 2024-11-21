# Part I

raw = open('data/everybody_codes_e2024_q11_p1.txt', 'r').readlines()

conv = {
    line.split(':')[0] : line.strip().split(':')[1].split(',')
    for line in raw
}

class Nest:
    def __init__(self, swarm={'A': 1}):
        self.swarm = swarm

    def propagate(self):
        new_bugs = {}
        for bug, count in self.swarm.items():
            for new_bug in conv[bug]:
                new_bugs[new_bug] = new_bugs.get(new_bug, 0) + count

        self.swarm = new_bugs

    def __repr__(self):
        return str(self.swarm)

    def __len__(self):
        return sum(v for k, v in self.swarm.items())

n = Nest()

for day in range(1, 5):
    n.propagate()

sol = len(n)
print(f"A ::: {sol}")

# Part II

raw = open('data/everybody_codes_e2024_q11_p2.txt', 'r').readlines()

conv = {
    line.split(':')[0] : line.strip().split(':')[1].split(',')
    for line in raw
}

n = Nest({'Z': 1})

for day in range(1, 11):
    n.propagate()

sol = len(n)
print(f"B ::: {sol}")

# Part III

raw = open('data/everybody_codes_e2024_q11_p2.txt', 'r').readlines()

#  conv = {
    #  line.split(':')[0] : line.strip().split(':')[1].split(',')
    #  for line in raw
#  }

conv = {
    'A': ['B', 'C'],
    'B': ['C', 'A', 'A'],
    'C': ['A']
}

all_keys = list(conv.keys())
all_values = []
for v in conv.values():
    all_values += v
all_values = list(set(all_values))
termites = list(set(all_keys + all_values))

def run_simulation(init, days=20):
    n = Nest({init: 1})

    for day in range(days):
        n.propagate()

    return len(n)

pops = {name: run_simulation(name) for name in termites}

min_key = min(pops, key=pops.get)
max_key = max(pops, key=pops.get)

sol = pops[max_key] - pops[min_key]

# Not 4403506530
# dn begin with 4, wrong len
print(f"C ::: {sol}")
