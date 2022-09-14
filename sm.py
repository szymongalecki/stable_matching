"""
readig from files : pipe file to the program as an input

cat friends_in.txt | python3 sm.py
cat illiad_in.txt | python3 sm.py
"""

n, names = 0, {}

# stdin
l = input()
while l.startswith("#"):
    l = input()
n = int(l[2:])

# map names
for _ in range(2 * n):
    key, val = input().split()
    names[int(key)] = val

# initialise data structures
P = list(range(1, 2 * n, 2))
P_preference = {key: [] for key in list(range(1, 2 * n, 2))}
R_preference = {key: {} for key in list(range(2, 2 * n + 1, 2))}
S = {key: -1 for key in list(range(2, 2 * n + 1, 2))}

# empty line between names and ranking
empty_line = input()

# fill in P_preference and R_preference
for _ in range(2 * n):
    key, pref = input().split(":")
    pref = [int(_) for _ in pref.split()]
    key = int(key)

    if key % 2 == 1:
        P_preference[key] = pref
    else:
        i = 1
        for p in pref:
            R_preference[key][p] = i
            i += 1

# stable matching algorithm
while P:
    # proposer, rejecter
    p = P.pop(0)
    r = P_preference[p].pop(0)

    # rejecter is unmarried -> marry
    if S[r] == -1:
        S[r] = p

    # proposer is more attractive than partner -> divorce partner, marry proposer
    elif R_preference[r][p] < R_preference[r][S[r]]:
        P.append(S[r])
        S[r] = p

    # unsuccesful proposal -> proposer goes back to pool
    else:
        P.append(p)

# invert matching dictionary: R:P -> P:R
S = {v: k for k, v in S.items()}

# print matching, ordered by proposers
for i in range(1, 2 * n, 2):
    print(f"{names[i]} -- {names[S[i]]}")
