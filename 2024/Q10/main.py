from string import ascii_uppercase
import numpy as np

# Part I

notes = open('data/everybody_codes_e2024_q10_p1.txt', 'r').readlines()

#  notes = """
#  **PCBS**
#  **RLNW**
#  BV....PT
#  CR....HZ
#  FL....JW
#  SG....MN
#  **FTZV**
#  **GMJH**
#  """.strip().split('\n')

mx = np.array([list(l.strip()) for l in notes])

rows, cols = np.where(mx == '.')
chars = []
for r, c in zip(rows, cols):
    hline = mx[r, :]
    vline = mx[:, c]
    chars.append(list(set(hline) & set(vline) - {'.'})[0])

sol = ''.join(chars)
print(f"A ::: {sol}")

# Part II
notes_raw = open('data/everybody_codes_e2024_q10_p2.txt', 'r').readlines()
mx = np.array([list(l.strip()) for l in notes_raw if l.strip()])

point_map = {char: i + 1 for i, char in enumerate(ascii_uppercase)}

def get_word(board):
    rows, cols = np.where(board == '.')
    chars = []
    for r, c in zip(rows, cols):
        hline = board[r, :]
        vline = board[:, c]
        chars.append(list(set(hline) & set(vline) - {'.'})[0])

    return ''.join(chars)

def score_word(word, point_map):
    return sum((pos + 1) * point_map.get(char) for pos, char in enumerate(word))

boards = []
for j in range(15):
    for i in range(7):
        b = mx[(8*i):(8*i + 8), (9*j):(9*j + 8)]
        boards.append(b)

words = [get_word(b) for b in boards]
scores = [score_word(w, point_map) for w in words]
sol = sum(scores)
print(f"B ::: {sol}")
