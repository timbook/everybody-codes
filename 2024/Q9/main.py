# Part I

stamps = [10, 5, 3, 1]

#  notes = [2, 4, 7, 16]

notes = open('data/everybody_codes_e2024_q09_p1.txt', 'r').readlines()
notes = [int(n.strip()) for n in notes]

def process_note(n, stamps):
    remaining = n
    total_beetles = 0
    for stamp in stamps:
        n_beetles = remaining // stamp
        print(f"Need {n_beetles} beetles since = {remaining} // {stamp}")
        total_beetles += n_beetles
        remaining -= n_beetles*stamp
    return total_beetles

beetles = [process_note(n, stamps) for n in notes]
sol = sum(beetles)

print(f"A ::: {sol}")

# Part II
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30][::-1]
notes = [33, 41, 55, 99]
#  notes = open('data/everybody_codes_e2024_q09_p1.txt', 'r').readlines()
#  notes = [int(n.strip()) for n in notes]

beetles = [process_note(n, stamps) for n in notes]
sol = sum(beetles)

# Note 123784
# wrong len, wrong 1
print(f"B ::: {sol}")
