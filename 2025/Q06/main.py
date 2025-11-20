# PART I =================================

# raw = "ABabACacBCbca"
raw = open('data/input1.txt', 'r').read().strip()
raw = open('data/input1.txt', 'r').read().strip()

n_mentor = 0
n_pairs = 0

for char in raw:
    if char == 'A':
        n_mentor += 1
    elif char == 'a':
        n_pairs += n_mentor

print(f"I :: {n_pairs}")

# PART II ================================

# raw = "ABabACacBCbca"
raw = open('data/input2.txt', 'r').read().strip()

is_mentor = lambda char: char.upper() == char

mentors = {}
n_pairs = 0

for char in raw:
    if is_mentor(char):
        mentors[char] = mentors.get(char, 0) + 1
    else:
        n_pairs += mentors[char.upper()]

print(f"II :: {n_pairs}")

# PART III ===============================

# raw = "AABCBABCABCabcabcABCCBAACBCa"
raw = open('data/input3.txt', 'r').read().strip()

D = 1000
R = 1000
data = R*raw

# Initialize
left = 0
right = min(D, len(data) - 1)
mentors = {}
n_pairs = 0

for char in data[left:right]:
    if is_mentor(char):
        mentors[char] = mentors.get(char, 0) + 1

char = data[0]
if char.islower():
    # print(f"At ptr = 0 -> {char} has {mentors.get(char.upper(), 0)} mentors.")
    # print(f"It scanned = {data[left:right+1]}")
    n_pairs += mentors.get(char.upper(), 0)

ptr = 0
while ptr < len(data):
    # Remove old left
    l_char = data[left]
    if max(0, ptr - D) != 0 and l_char.isupper():
        mentors[l_char] = mentors[l_char] - 1
    left = max(0, ptr - D)

    # Add new right
    right = min(ptr + D, len(data) - 1)
    r_char = data[right]
    if right < len(data) and r_char.isupper():
        mentors[r_char] = mentors[r_char] + 1

    # Add mentors if current char is lowercase
    char = data[ptr]
    if char.islower():
        # print(f"At ptr = {ptr} -> {char} has {mentors.get(char.upper(), 0)} mentors.")
        # print(f"It scanned = {data[left:right+1]}")
        n_pairs += mentors.get(char.upper(), 0)

    # Increment ptr
    ptr += 1

# 1667272483 correct len correct first char
print(f"III :: {n_pairs}")
