import random

##This simulates tests relays where the first fencer
##has a probabilty of f1 of winning, the second
##fencer has a probability of f2 of winning, and
##the third fencer has a probability of f3 of
##winning.  The output is the amount of relays
##you win.
def simulate(f1, f2, f3, tests):
    wins = 0
    for i in range(tests):
        pu = 0
        pt = 0
        while ((pu < 15) and (pt < 15)):
            r = random.random()
            if (r < f1):
                pu += 1
            if (r > f1):
                pt += 1
        while ((pu < 30) and (pt < 30)):
            r = random.random()
            if (r < f2):
                pu += 1
            if (r > f2):
                pt += 1
        while ((pu < 45) and (pt < 45)):
            r = random.random()
            if (r < f3):
                pu += 1
            if (r > f3):
                pt += 1

        if (pu == 45):
            wins += 1
    return(wins)

print(simulate(.25, .5, .75, 1000000))
print(simulate(.25, .75, .5, 1000000))
print(simulate(.5, .25, .75, 1000000))
print(simulate(.5, .75, .25, 1000000))
print(simulate(.75, .25, .5, 1000000))
print(simulate(.75, .5, .25, 1000000))
