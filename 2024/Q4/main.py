import numpy as np

# Part I
data = [int(l.strip()) for l in open('data/everybody_codes_e2024_q4_p1.txt', 'r').readlines()]
m = min(data)
sol = sum(value - m for value in data)
print(f"1 ::: {sol}")

# Part II
data = [int(l.strip()) for l in open('data/everybody_codes_e2024_q4_p2.txt', 'r').readlines()]
m = min(data)
sol = sum(value - m for value in data)
print(f"2 ::: {sol}")

# Part III
data = np.array([int(l.strip()) for l in open('data/everybody_codes_e2024_q4_p3.txt', 'r').readlines()])
med = np.median(data)
sol = np.sum(np.abs(data - med)).astype(int)
print(f"3 ::: {sol}")
