import numpy as np
import pandas as pd

class Vertibra:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        left = f"{self.left}-" if self.left else ""
        right = f"-{self.right}" if self.right else ""
        return f"{left}{self.data}{right}"

    def to_str(self):
        left = str(self.left) if self.left else ''
        right = str(self.right) if self.right else ''
        return left + str(self.data) + right

def quality(sword):
    spine = [v.data for v in sword]
    return int(''.join([str(n) for n in spine]))

def make_sword(data):
    sword = [Vertibra(data[0])]
    for n in data[1:]:
        found = False
        for vert in sword:
            if n < vert.data and vert.left is None and not found:
                vert.left = n
                found = True
            elif n > vert.data and vert.right is None and not found:
                vert.right = n
                found = True
        if not found:
            sword.append(Vertibra(n))
    return sword

def grade_line(data):
    sword = make_sword(data)
    return quality(sword)

def get_sort_str(sword):
    return ''.join([v.to_str().rjust(3, '0') for v in sword])
    

# PART I =================================

raw = open('data/input1.txt', 'r').read().strip()

sid, num_str = raw.split(':')
data = [int(n) for n in num_str.split(',')]


sol = grade_line(data)

print(f"I :: {sol}")

# PART II ================================

lines = open('data/input2.txt', 'r').readlines()
data = [line.strip().split(':')[1] for line in lines]
data = [[int(d) for d in line.split(',')] for line in data]

qualities = [grade_line(d) for d in data]
sol = max(qualities) - min(qualities)
print(f"II :: {sol}")

# PART III ===============================

lines = open('data/input3.txt', 'r').readlines()
sids = [int(line.strip().split(':')[0]) for line in lines]
data = [line.strip().split(':')[1] for line in lines]
data = [[int(d) for d in line.split(',')] for line in data]

swords = [make_sword(d) for d in data]
grades = [grade_line(d) for d in data]
sword_strs = [get_sort_str(sw) for sw in swords]
swords_full = [(sid, sw) for sid, sw in zip(sids, sword_strs)]

swords_full = [(sid, gr, sw) for sid, gr, sw in zip(sids, grades, sword_strs)]
df = pd.DataFrame(swords_full, columns=['sid', 'grade', 'sword']) \
    .sort_values(['grade', 'sword', 'sid'], ascending=False)
df['new_sid'] = np.arange(1, df.shape[0] + 1)

sol = sum(df.sid * df.new_sid)
print(f"III :: {sol}")

