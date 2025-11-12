raw = open('data/input1.txt', 'r').readlines()

names = raw[0].strip().split(',')
data = raw[2].strip().split(',')

L = len(names)
ptr = 0

def print_name(p):
    print(f"Your name is now {names[p]}")

for move in data:
    direction = move[0]
    step = int(move[1:])
    ptr = ptr + step*(2*(direction == 'R') - 1)
    ptr = min(max(0, ptr), L - 1)

sol = names[ptr]
print(f"A ::: {sol}")

raw = open('data/input2.txt', 'r').readlines()

names = raw[0].strip().split(',')
data = raw[2].strip().split(',')

L = len(names)
ptr = 0

for move in data:
    direction = move[0]
    step = int(move[1:])
    ptr = ptr + step*(2*(direction == 'R') - 1)
    ptr = ptr % L

sol = names[ptr]
print(f"B ::: {sol}")

raw = open('data/input3.txt', 'r').readlines()

names = raw[0].strip().split(',')
data = raw[2].strip().split(',')

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

L = len(names)
ptr = 0

for move in data:
    direction = move[0]
    step = int(move[1:])
    ptr = step*(2*(direction == 'R') - 1) % L
    swap(names, 0, ptr)

sol = names[0]
print(f"C ::: {sol}")
