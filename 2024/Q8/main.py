from functools import reduce

# Part I

note = 4_099_126

n = note**0.5 // 1 + 1

L = lambda n: 2*n - 1
T = lambda n: n**2

target_width = L(n)
missing_blocks = T(n) - note
sol = int(target_width*missing_blocks)

print(f"A ::: {sol}")

# Part II

note = 397
acolytes = 1111
avail_blocks = 20_240_000

layer = 1
thickness = 1
blocks_needed = 0

while True:
    blocks_needed += thickness*L(layer)
    if blocks_needed >= avail_blocks:
        break
    layer += 1
    thickness = (thickness * note) % acolytes

target_width = L(layer)
missing_blocks = blocks_needed - avail_blocks
sol = int(target_width*missing_blocks)
print(f"B ::: {sol}")

# Part III
# TODO
