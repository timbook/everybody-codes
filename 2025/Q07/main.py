from itertools import pairwise

def process_input(raw):
    names = raw[0].strip().split(',')
    lines = [line.strip() for line in raw[2:]]

    char_map = {}
    for line in lines:
        lhs, rhs = line.strip().split(' > ')
        char_map[lhs] = rhs.replace(',', '')

    return names, char_map

def name_ok(name, char_map):
    for a, b in pairwise(name):
        if b not in char_map[a]:
            return False
    return True

# PART I ======================================

raw = open('data/input1.txt', 'r').readlines()
names, char_map = process_input(raw)

for name in names:
    if name_ok(name, char_map):
        sol = name
        break

print(f"I :: {sol}")

# PART II =====================================

raw = open('data/input2.txt', 'r').readlines()
names, char_map = process_input(raw)

good_names = [i + 1 for i, name in enumerate(names) if name_ok(name, char_map)]
sol = sum(good_names)

print(f"II :: {sol}")

# PART III ====================================

raw = open('data/input3.txt', 'r').readlines()

prefixes, char_map = process_input(raw)

def backtrack(curr_name, solutions, char_map):
    # If done, record it
    if 7 <= len(curr_name) <= 11:
        solutions.append(''.join(curr_name))

    if len(curr_name) == 11:
        return

    if curr_name[-1] not in char_map:
        return

    # For each next step
    for char in char_map[curr_name[-1]]:
        curr_name.append(char)
        backtrack(curr_name, solutions, char_map)
        curr_name.pop()

sols = []
for pre in prefixes:
    if name_ok(pre, char_map):
        backtrack(list(pre), sols, char_map)

sol = len(set(sols))
print(f"III :: {sol}")

