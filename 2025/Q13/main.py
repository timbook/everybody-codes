from collections import deque

class Span:
    def __init__(self, text, rev=False):
        self.rev = rev
        if isinstance(text, int):
            self.a = text
            self.b = text
        else:
            a, b = text.strip().split('-')
            self.a = int(a)
            self.b = int(b)

        if rev:
            self.a, self.b = self.b, self.a

        self._len = abs(self.b - self.a) + 1

    def __len__(self):
        return self._len

    def __repr__(self):
        return f"{self.a}:{self.b}"

    def __getitem__(self, i):
        if not self.rev:
            return self.a + i - 1
        else:
            return self.a - i + 1

# PART I ======================================== 

# raw = open('data/sample1.txt').readlines()
raw = open('data/input1.txt').readlines()
data = [int(n.strip()) for n in raw]

dial = deque([1])

for i, n in enumerate(data):
    if i % 2 == 0:
        dial.append(n)
    else:
        dial.appendleft(n)

ptr = dial.index(1)
sol = dial[(ptr + 2025) % len(dial)]
print(f"I :: {sol}")

# PART II ======================================== 

# raw = open('data/sample2.txt').readlines()
raw = open('data/input2.txt').readlines()
data = [n.strip() for n in raw]

dial = deque([Span(1, 1)])

ptr = 0
for i, text in enumerate(data):
    if i % 2 == 0:
        dial.append(Span(text))
    else:
        dial.appendleft(Span(text, rev=True))
        ptr += 1

remainder = 20252025 % sum(len(s) for s in dial)

while True:
    ptr = (ptr + 1) % len(dial)
    curr = dial[ptr]
    if len(curr) < remainder:
        remainder -= len(curr)
    else:
        sol = curr[remainder]
        break

print(f"II :: {sol}")

# PART III ======================================= 

raw = open('data/input3.txt').readlines()
data = [n.strip() for n in raw]
dial = deque([Span(1, 1)])

ptr = 0
for i, text in enumerate(data):
    if i % 2 == 0:
        dial.append(Span(text))
    else:
        dial.appendleft(Span(text, rev=True))
        ptr += 1

remainder = 202520252025 % sum(len(s) for s in dial)

while True:
    ptr = (ptr + 1) % len(dial)
    curr = dial[ptr]
    if len(curr) < remainder:
        remainder -= len(curr)
    else:
        sol = curr[remainder]
        break

print(f"III :: {sol}")
