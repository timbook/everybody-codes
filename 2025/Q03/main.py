# PART I =============================

raw = open('data/input1.txt', 'r').read().strip()
data = [int(n) for n in raw.split(',')]

sol = sum(set(data))
print(f"I :: {sol}")

# PART II ============================

raw = open('data/input2.txt', 'r').read().strip()
data = [int(n) for n in raw.split(',')]

smallest_creates = sorted(list(set(data)))
sol = sum(smallest_creates[:20])
print(f"II :: {sol}")

# PART III ===========================

raw = open('data/input3.txt', 'r').read().strip()
data = [int(n) for n in raw.split(',')]

import pandas as pd

s = pd.Series(data)
sol = s.value_counts().values[0]
print(f"III :: {sol}")
