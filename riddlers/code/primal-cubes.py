import itertools

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

octuples = itertools.permutations(primes, 8)
valid = []

for l in octuples:
    if ((l[0] + l[1] == l[4] + l[5]) and
        (l[2] + l[3] == l[6] + l[7]) and
        (l[0] + l[3] == l[5] + l[6]) and
        (l[1] + l[2] == l[4] + l[7])):
        valid.append(l)
        print(l)

print(len(valid)//48)
