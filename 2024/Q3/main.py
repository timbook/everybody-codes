import numpy as np

# Part I
grid_raw = np.genfromtxt('data/everybody_codes_e2024_q3_p1.txt', dtype=str, delimiter=1, comments='Z')
grid = np.where(grid_raw == '#', 1, 0)

class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.gen_dig_sites()

    def __repr__(self):
        return '\n'.join([''.join(row) for row in self.grid.astype(str)])

    def get_neighbors(self, r, c):
        nbs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        nbs = [nb for nb in nbs if 0 <= nb[0] < self.grid.shape[0] and 0 <= nb[1] < self.grid.shape[1]]
        return nbs

    def gen_dig_sites(self):
        dig_rows, dig_cols = np.where(self.grid > 0)
        self.dig_sites = {(r, c) for r, c in zip(dig_rows, dig_cols)}

    def dig_once(self):
        grid_new = self.grid.copy()
        for r, c in self.dig_sites:
            nbs = self.get_neighbors(r, c)
            my_val = self.grid[r, c]
            nb_vals = np.array([self.grid[nb[0], nb[1]] for nb in nbs])
            dig_here = np.all(my_val == nb_vals)
            if dig_here:
                grid_new[r, c] = my_val + 1
        self.grid = grid_new

    def dig(self):
        while True:
            old_grid = self.grid.copy()
            self.dig_once()
            if np.all(old_grid == self.grid):
                break

    def volume(self):
        return np.sum(self.grid)

g = Grid(grid)
g.dig()
sol = g.volume()
print(f"I ::: {sol}")

# Part II
grid_raw = np.genfromtxt('data/everybody_codes_e2024_q3_p2.txt', dtype=str, delimiter=1, comments='Z')
grid = np.where(grid_raw == '#', 1, 0)
g = Grid(grid)
g.dig()
sol = g.volume()
print(f"II ::: {sol}")

# Part III
grid_raw = np.genfromtxt('data/everybody_codes_e2024_q3_p3.txt', dtype=str, delimiter=1, comments='Z')
grid = np.where(grid_raw == '#', 1, 0)
grid = np.pad(grid, 1)

class GridDiag(Grid):
    def get_neighbors(self, r, c):
        nbs = [
            (r - 1, c - 1), (r - 1, c    ), (r - 1, c + 1),
            (r    , c - 1), (r    , c    ), (r    , c + 1),
            (r + 1, c - 1), (r + 1, c    ), (r + 1, c + 1)
        ]
        nbs = [nb for nb in nbs if 0 <= nb[0] < self.grid.shape[0] and 0 <= nb[1] < self.grid.shape[1]]
        return nbs

g = GridDiag(grid)
g.dig()
sol = g.volume()
print(f"III ::: {sol}")
