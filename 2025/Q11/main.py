from itertools import pairwise

def checksum(data):
    return sum(k*v for k, v in data.items())

def run_sim1(data):
    for i, j in pairwise(range(1, len(data) + 1)):
        if data[i] > data[j]:
            data[i] -= 1
            data[j] += 1
    return data

def run_sim2(data):
    for i, j in pairwise(range(1, len(data) + 1)):
        if data[i] < data[j]:
            data[i] += 1
            data[j] -= 1
    return data

def phase1(data):
    counter = 0
    prev_sum = checksum(data)
    while True:
        data = run_sim1(data)
        curr_sum = checksum(data)
        if prev_sum == curr_sum:
            break
        prev_sum = curr_sum
        counter += 1

    return data, counter

def phase2(data, counter, until=None):
    while True:
        data = run_sim2(data)
        counter += 1

        if until and counter >= until:
            break

        if all(v == data[1] for k, v in data.items()):
            break

    return data, counter

# PART I =============================================

# raw = [9, 1, 1, 4, 9, 6]
raw = [1, 17, 19, 19, 14, 14]

data = {i + 1: n for i, n in enumerate(raw)}

data, rnd = phase1(data)
data, rnd = phase2(data, rnd, 10)
sol = checksum(data)

print(f"I :: {sol}")

# PART II ============================================

# raw = [9, 1, 1, 4, 9, 6]
# raw = [805, 706, 179, 48, 158, 150, 232, 885, 598, 524, 423]
# data = {i + 1: n for i, n in enumerate(raw)}
raw = open('data/input2.txt').readlines()
data = {i + 1: int(n.strip()) for i, n in enumerate(raw)}

# data, rnd = phase1(data)
# print(f"Phase I concludes at round {rnd}")
# data, rnd = phase2(data, rnd)
# print(f"II :: {rnd}")

# PART III ===========================================

raw = open('data/input3.txt').readlines()
data = {i + 1: int(n.strip()) for i, n in enumerate(raw)}
data, rnd = phase1(data)
print(f"Phase I concludes at round {rnd}")
data, rnd = phase2(data, rnd)
print(f"III :: {rnd}")
