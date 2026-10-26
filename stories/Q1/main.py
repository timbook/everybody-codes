import re

def eni(n, exp, mod):
    score = 1
    remainders = []
    for _ in range(exp):
        score *= n
        score %= mod
        remainders.append(score)
    return int(''.join(str(i) for i in remainders[::-1]))

def proc_row(row):
    nums = re.findall(r'\d+', row)
    nums = [int(i) for i in nums]
    a, b, c, x, y, z, m = nums
    return eni(a, x, m) + eni(b, y, m) + eni(c, z, m)

with open('data/input1.txt', 'r') as f:
    lines = f.readlines()

sols = [proc_row(row) for row in lines]
sol = max(sols)

print(f'A ::: {sol}')

# ============================================================================

def power_mod(n, exp, mod):
    res = 1
    n %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * n) % mod
        n = (n * n) % mod
        exp //= 2
    return res

def eni_b(n, exp, mod):
    remainders = [power_mod(n, exp - i, mod) for i in range(5) if exp - i > 0]
    return int(''.join(str(i) for i in remainders))

def proc_row_b(row):
    nums = re.findall(r'\d+', row)
    nums = [int(i) for i in nums]
    a, b, c, x, y, z, m = nums
    return eni_b(a, x, m) + eni_b(b, y, m) + eni_b(c, z, m)

with open('data/input2.txt', 'r') as f:
    lines = f.readlines()

sols = [proc_row_b(row) for row in lines]
sol = max(sols)

print(f'B ::: {sol}')

# ============================================================================

with open('data/sample3a.txt', 'r') as f:
    lines = f.readlines()

def ingest_row(row):
    nums = re.findall(r'\d+', row)
    return [int(i) for i in nums]
    # a, b, c, x, y, z, m = nums

def eni_c(n, exp, mod):
    score = 1
    seq = []
    for _ in range(mod - 1):
        score *= n
        score %= mod
        seq.append(score)
    L = len(seq)
    S = sum(seq)
    return S*(exp // L) + sum(seq[:(exp % L)])

def proc_row_c(nums):
    a, b, c, x, y, z, m = nums
    return eni_c(a, x, m) + eni_c(b, y, m) + eni_c(c, z, m)
    
sols = [proc_row_c(ingest_row(row)) for row in lines]
sol = max(sols)
print(f'C ::: {sol}')
