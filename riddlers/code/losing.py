import random
import math

##This is computes the probability that the Birds win if
##their lead is by x and there are y flips remaining.
def f(x, y):
    total = 0
    for i in range((x+y+1)//2):
        total += math.comb(y, i)
    total = total/(2**y)
    return(total)

##This generates a random sequence of +/-1s of length k
def genseq(k):
    result = []
    for i in range(k):
        result.append(random.randrange(-1, 3, 2))
    return(result)

##This checks to see if the Birds lose if seq is the
##sequence of flips.
def loses(seq):
    k = len(seq)
    total = 0
    for i in range(k):
        total += seq[i]
    return((total < 0))

##This checks to see if the Birds have a least a tol chance
##of winning the game at some point if the sequence of flips
##is seq.
def shouldwin(seq, tol):
    k = len(seq)
    x = 0
    y = k
    for i in range(k):
        y -= 1
        x += seq[i]
        if(f(x, y) > tol):
            return(True)
    return(False)

##This simulates sims games that are k flips long and tells you
##how many games the Birds had a tol chance of winning at some
##point as well as how many games they wound up losing after
##having a tol chance of winning.
def simulate(k, sims, tol):
    potwins = 0
    losses = 0
    for i in range(sims):
        s = genseq(k)
        if(shouldwin(s, tol)):
            potwins += 1
            if(loses(s)):
                losses += 1
    print(sims, potwins, losses)

simulate(101, 1000000, .99)
