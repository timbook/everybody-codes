import itertools 

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(
            self.x*other.x - self.y*other.y,
            self.x*other.y + self.y*other.x
        )

    def __truediv__(self, other):
        return Vector(
            self.x // other.x if self.x >= 0 else -((-self.x) // other.x),
            self.y // other.y if self.y >= 0 else -((-self.y) // other.y)
        )

    def __repr__(self):
        return f"[{self.x},{self.y}]"

    def is_engraved(self):
        v = Vector(0, 0)
        for i in range(100):
            v = v * v
            v = v / Vector(100_000, 100_000)
            v = v + self
            if abs(v.x) > 1_000_000 or abs(v.y) > 1_000_000:
                return False
        return True
            

def vector_cycle(v, a):
    v = v * v
    v = v / Vector(10, 10)
    return v + a

def cycle_n(v, a, n):
    for _ in range(n):
        v = vector_cycle(v, a)
    return v

z = Vector(0, 0)
a = Vector(164, 50)

res = cycle_n(z, a, 3)

print(f"A :: {res}")

a = Vector(-3294, 68783)

points = {}

for r, c in itertools.product(range(101),range(101)):
    point = Vector(a.x + 10*r, a.y + 10*c)
    points[(point.x, point.y)] = point.is_engraved()

sol = [k for k, v in points.items() if v]

print(f"B :: {len(sol)}")

a = Vector(-3294, 68783)

points = {}

for r, c in itertools.product(range(1001),range(1001)):
    point = Vector(a.x + r, a.y + c)
    points[(point.x, point.y)] = point.is_engraved()

sol = [k for k, v in points.items() if v]

print(f"C :: {len(sol)}")
