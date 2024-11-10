import re
import numpy as np
from collections import deque

# Part I
raw = open('data/everybody_codes_e2024_q2_p1.txt', 'r').readlines()
words = raw[0].split(':')[1].strip().split(',')
text = raw[2].strip()
sol = sum([text.count(word) for word in words])
print(f'A ::: {sol}')

# Part II
raw = open('data/everybody_codes_e2024_q2_p2.txt', 'r').readlines()
words = raw[0].split(':')[1].strip().split(',')
text = [line.strip() for line in raw[2:]]

sol = 0
for line in text:
    line_bits = np.zeros(len(line), dtype=bool)
    line_bits_rev = np.zeros(len(line), dtype=bool)

    for word in words:
        for m in re.finditer(word, line):
            line_bits[m.start():m.end()] = True
        for m in re.finditer(word, line[::-1]):
            line_bits_rev[m.start():m.end()] = True

    line_mask = line_bits | line_bits_rev[::-1]
    sol += sum(line_mask)

print(f"B ::: {sol}")

# Part III
raw = open('data/everybody_codes_e2024_q2_p3.txt', 'r').readlines()
words = raw[0].split(':')[1].strip().split(',')
text_mx = np.array([list(line.strip()) for line in raw[2:]])
text_mx_bool = np.zeros_like(text_mx, dtype=bool)
NROW, NCOL = text_mx.shape

def scan_row(row, words):
    line = ''.join(row)
    L = len(line)
    line_bits = np.zeros(3*L, dtype=bool)
    line_bits_rev = np.zeros(3*L, dtype=bool)

    for word in words:
        for m in re.finditer(word, 3*line):
            line_bits[m.start():m.end()] = True
        for m in re.finditer(word, 3*line[::-1]):
            line_bits_rev[m.start():m.end()] = True

    line_mask = line_bits | line_bits_rev[::-1]
    return line_mask[L:2*L]

def scan_col(col, words):
    line = ''.join(col)
    L = len(line)
    line_bits = np.zeros(L, dtype=bool)
    line_bits_rev = np.zeros(L, dtype=bool)

    for word in words:
        for m in re.finditer(word, line):
            line_bits[m.start():m.end()] = True
        for m in re.finditer(word, line[::-1]):
            line_bits_rev[m.start():m.end()] = True

    line_mask = line_bits | line_bits_rev[::-1]
    return line_mask

text_map_rows = np.array([scan_row(row, words) for row in text_mx])
text_map_cols = np.array([scan_col(col, words) for col in text_mx.T])

text_map = text_map_rows | text_map_cols.T
sol = np.sum(text_map)
print(f"C ::: {sol}")
