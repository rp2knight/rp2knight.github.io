import itertools
import math

##top is the highest value of C I search for.  solns
##is a list of all the valid triples (A, B, C, R).
##small is the smallest value of R I have found so far.
##best is the triple with the smallest value of R.
##checks is a list of all possible triples (A, B, C)

top = 100
solns = []
small = top*2
best = []
checks = itertools.combinations(range(1, top+1), 3)

##This loop finds all solutions and determines which one
##has the smallest value of R.

for check in checks:
    a = check[0]
    b = check[1]
    c = check[2]
    if(16*(b**2)-8*(a**2)-8*(c**2) > 0):
        if(((a**2 - c**2)**2) % (16*(b**2)-8*(a**2)-8*(c**2)) == 0):
            r = math.sqrt(((a**2 - c**2)**2) // (16*(b**2)-8*(a**2)-8*(c**2)) + b**2)
            if r.is_integer():
                solns.append([a, b, c, r])
                if (r < small):
                    small = r
                    best = [a, b, c, r]

print(solns)
print(best)
