import re

lines = open('data/input1.txt', 'r').readlines()

def score_line(line):
    data = [re.findall(r'(\d+)([<>])(\d+)', item)[0] for item in line.split(' ')]
    blade_labels = set([a for a, sym, b in data] + [b for a, sym, b in data])

    scores = {char: 0 for char in blade_labels}
    for a, sym, b in data:
        if sym == '<':
            scores[b] = scores.get(b, 0) + 1
        else:
            scores[a] = scores.get(a, 0) + 1

    return scores

def checksum(scores):
    scores_ordered = sorted(
        tuple(scores.items()),
        key=lambda t: t[1],
        reverse=True
    )
    return int(''.join(a for a, b in scores_ordered))

scores = [score_line(line) for line in lines]
checksums = [checksum(score) for score in scores]
sol = sum(checksums)
print(f'A ::: {sol}')

# ========================================================================

lines = open('data/sample2.txt', 'r').readlines()
