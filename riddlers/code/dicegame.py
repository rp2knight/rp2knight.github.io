import itertools
import math

##This funtion takes in a guess and a set of rolls,
##and outputs whether that guess wins for that set
##of rolls.

def win(g, r):
    for a in g:
        for b in itertools.combinations(r, 2):
            if b[0] + b[1] == a:
                return(True)
    return(False)

##This function takes in a guess and a set of sets
##of rolls, and determines how many of the rolls
##the guess wins for.

def score(g, rs):
    score = 0
    for r in rs:
        if win(g, r):
            score += 1
    return(score)

##gu is the number of guesses, ro is the number of rolls,
##and si is the number of sides of the die.

gu = 4
ro = 4
si = 6

##This part loops over all the (sensible) guesses and finds
##the best guess(es) and the worst guess(es), and prints out
##both how good they are and what they are.  In addition, it
##finds out how good a random guess is on average.

guesses = itertools.combinations(range(2, 2*si+1), gu)

tot = 0
best = 0
bests = []
worst = si**ro
worsts = []

for guess in guesses:
    rolls = itertools.product(range(1, si+1), repeat=ro)
    s = score(guess, rolls)
    tot += s
    if s == best:
        bests.append(guess)
    if s > best:
        best = s
        bests = [guess]
    if s == worst:
        worsts.append(guess)
    if s < worst:
        worst = s
        worsts = [guess]
    
print(best, best/(si**ro), bests)
print(worst, worst/(si**ro), worsts)
print(tot/(math.comb(2*si-1, gu)*(si**ro)))
