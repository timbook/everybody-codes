# Part I

data = open('data/everybody_codes_e2024_q1_p1.txt', 'r').read().strip()
point_map = {'A': 0, 'B': 1, 'C': 3}
potions = [point_map.get(char) for char in data]
sol = sum(potions)
print(f'A ::: {sol}')

# Part II

data = open('data/everybody_codes_e2024_q1_p2.txt', 'r').read().strip()
point_map = {'A': 0, 'B': 1, 'C': 3, 'D': 5}

sol = 0
for i1, i2 in zip(data[::2], data[1::2]):
    n_bugs = 2 - (i1 + i2).count('x')
    bonus_points = 0 if n_bugs <= 1 else 2
    potions = point_map.get(i1, 0) + point_map.get(i2, 0) + bonus_points
    sol += potions

print(f'B ::: {sol}')

# Part III

data = open('data/everybody_codes_e2024_q1_p3.txt', 'r').read().strip()
#  data = 'xBxAAABCDxCC'
point_map = {'A': 0, 'B': 1, 'C': 3, 'D': 5}

sol = 0
while data:
    battle = data[:3]
    data = data[3:]

    n_bugs = 3 - battle.count('x')
    bonus_points = {1: 0, 2: 2, 3: 6}.get(n_bugs, 0)
    potions = sum([point_map.get(char, 0) for char in battle]) + bonus_points
    sol += potions

print(f'C ::: {sol}')
