# PART I ======================

sol = int(1000 / 182 * 2025)
print(f"I :: {sol}")

# PART II =====================

const = 10000000000000

sol = int(const / (994 / 278)) + 1
print(f"II :: {sol}")

# PART II =====================

raw = open('data/input3.txt', 'r').readlines()
lines = [l.strip() for l in raw]

data_raveled = [int(lines[0])] + [
    (int(l.split('|')[0]), int(l.split('|')[1]))
    for l in lines[1:-1]
] + [int(lines[-1])]

data = []
for item in data_raveled:
    if isinstance(item, int):
        data.append(item)
    elif isinstance(item, tuple):
        data.extend(list(item))

data_rev = data[::-1].copy()

res = 1
while data_rev:
    num = data_rev.pop()
    denom = data_rev.pop()
    res *= (num / denom)

sol = int(100*res)
print(f"III :: {sol}")
