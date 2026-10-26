import numpy as np

class Board:
    def __init__(self, mx):
        self.grid = mx
        self.R, self.C = self.grid.shape

    def tick(self):
        grid_next = self.grid.copy()

        for r in range(self.R):
            for c in range(self.C):
                nbs = [
                    (r + 1, c + 1), (r + 1, c - 1),
                    (r - 1, c + 1), (r - 1, c - 1)
                ]
                nbs = np.array([
                    self.grid[r, c] for r, c in nbs
                    if 0 <= r < self.R and 0 <= c < self.C
                ])
                n_active = sum(nbs == '#')

                if self.grid[r, c] == '#':
                    grid_next[r, c] = '#' if n_active % 2 == 1 else '.'
                else:
                    grid_next[r, c] = '#' if n_active % 2 == 0 else '.'

        self.grid = grid_next

    def score(self):
        return np.sum(self.grid == '#')

    def __repr__(self):
        return '\n'.join([''.join(row) for row in self.grid])

# PART I ============================================= 

# raw = open('data/sample1.txt', 'r').readlines()
raw = open('data/input1.txt', 'r').readlines()

mx = np.array([list(line.strip()) for line in raw])

board = Board(mx)

score = 0
for _ in range(10):
    board.tick()
    score += board.score()

print(f"I :: {score}")

# PART II ============================================= 

raw = open('data/input2.txt', 'r').readlines()

mx = np.array([list(line.strip()) for line in raw])

board = Board(mx)

score = 0
for _ in range(2025):
    board.tick()
    score += board.score()

print(f"II :: {score}")
