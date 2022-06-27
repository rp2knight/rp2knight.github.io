##This checks to see if you can put a goat in that prefers
##room j.  If you can, it returns an array whose 0th entry
##is True and whose first entry is the code of the new tower.
##If you can't, it returns an array whose 0th term is False.
def insert(i, j, k):
    p = i
    while(p < k):
        if (2**p ^ j) == (2**p + j):
            return([True, 2**p + j])
        p += 1
    return([False])

##This is the main loop that computes the probabilities
##recursively.  Technically, since you know that the
##denominator of a tower with a open rooms is n^a, this
##actually computes the probability times n^a so that you
##don't have to deal with floats and rounding errors and
##so on.
n = 10

probs = [0]*(2**n)
probs[2**n - 1] = 1

for i in range(2**n - 2, -1, -1):
    tot = 0
    for j in range(n):
        a = insert(j, i, n)
        if a[0]:
            tot += probs[a[1]]
    probs[i] = tot

print(probs)
