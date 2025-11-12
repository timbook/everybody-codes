data_raw = open('./sample.txt', 'r').readlines()

inits = data_raw[0].strip().split(',')
inits = [int(i) for i in inits]

lines_raw = data_raw[2:]
lines = [list(l) for l in lines_raw]

class Column:
    def __init__(self, faces, step):
        self.step = step
        self.faces = faces
        self.pos = 0

    def advance_n(self, n):
        self.pos = (self.pos + n * self.step) % n

    def advance(self):
        self.advance_n(1)

    @property
    def face(self):
        return self.faces[self.pos]

def advance_cols(cols, n):
    for c in cols:
        c.advance_n(n)

def score_cols(cols):
    s = ''.join([c.face for c in cols])
    chars = {}
    for char in s:
        chars[char] = chars.get(char, 0) + 1

    points = 0
    for char, n in chars.items():
        if n >= 3:
            points += (n - 2)

    return points

def print_cols(cols):
    print(' '.join([c.face for c in cols]))

cols = []
for i, init in enumerate(inits):
    faces = [''.join(l[4*i:4*i + 3]) for l in lines]
    faces = [f for f in faces if f.strip()]
    col = Column(faces, init)
    cols.append(col)

