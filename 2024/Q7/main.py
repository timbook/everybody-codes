from itertools import cycle
from functools import reduce
import numpy as np

# Part I

def extend_track(track, L):
    res = []
    c = cycle(track)
    for _ in range(L):
        res.append(next(c))        
    return res

raw = open('data/everybody_codes_e2024_q07_p1.txt', 'r').readlines()

L = 10

track = {}
for line in raw:
    horse, plan = line.strip().split(':')
    track[horse] = extend_track(plan.split(','), L)

scores = {}
for horse, plan in track.items():
    acc = 10
    cum_plan = []
    for step in plan:
        if step == '+':
            acc += 1
        elif step == '-':
            acc = max(acc - 1, 0)
        cum_plan.append(acc)

    scores[horse] = cum_plan

scores_sum = {k:sum(v) for k, v in scores.items()}
scores_sorted = sorted(scores_sum.items(), key=lambda t: t[1])
sol = ''.join([s[0] for s in scores_sorted])[::-1]

print(f"A ::: {sol}")

# Part II

raw = open('data/everybody_codes_e2024_q07_p2.txt', 'r').readlines()

track_raw = """
S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-
""".strip().split('\n')

horses = {}
for line in raw:
    horse, plan = line.strip().split(':')
    horses[horse] = plan.split(',')

track_mx = np.array([list(row) for row in track_raw])
track = track_mx[0, 1:].tolist() + \
    track_mx[1:, -1].tolist() + \
    track_mx[-1, :-1].tolist()[::-1] + \
    track_mx[:-1, 0].tolist()[::-1]

N_LOOPS = 10
scores = {}
for horse, plan in horses.items():

    acc = 10
    cum_plan = []
    plan_cycle = cycle(plan)
    for track_step in N_LOOPS*track:
        plan_step = next(plan_cycle)
        if track_step in '=S':
            if plan_step == '+':
                acc += 1
            elif plan_step == '-':
                acc = max(acc - 1, 0)
        else:
            if track_step == '+':
                acc += 1
            elif track_step == '-':
                acc = max(acc - 1, 0)
        cum_plan.append(acc)
    scores[horse] = cum_plan

scores_sum = {k:sum(v) for k, v in scores.items()}
scores_sorted = sorted(scores_sum.items(), key=lambda t: t[1])
sol = ''.join([s[0] for s in scores_sorted])[::-1]

print(f"B ::: {sol}")

# Part III

raw = open('data/everybody_codes_e2024_q07_p3.txt', 'r').readlines()

track_raw = """
S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-
""".strip().split('\n')

track_mx = np.array([list(l) for l in track_raw])
