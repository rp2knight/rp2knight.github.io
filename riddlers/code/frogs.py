import math
import matplotlib.pyplot as plt

##This code starts off with an implementation of the
##dyadic rationals, where a/2^n is represented as [a, n].
##dy(a) takes in an integer and returns it as a dyadic
##rational.  plus and times add and multiply two dyadic
##rationals.  simp simplifies a dyadic rational, removing
##superfluous powers of two from the denominator.  value
##spits out the value of the dyadic rational as a float.
def dy(a):
    return [a, 0]

def plus(d1, d2):
    a1 = d1[0]
    a2 = d2[0]
    n1 = d1[1]
    n2 = d2[1]
    if (n1 >= n2):
        n = n1
        a = a1 + (2**(n1-n2))*a2
    if (n2 > n1):
        n = n2
        a = a2 + (2**(n2-n1))*a1
    return([a, n])

def times(d1, d2):
    a1 = d1[0]
    a2 = d2[0]
    n1 = d1[1]
    n2 = d2[1]
    return([a1*a2, n1+n2])

def simp(d):
    a = d[0]
    n = d[1]
    while ((a % 2 == 0) and (n > 0)):
        a = a//2
        n = n-1
    return([a, n])

def value(d):
    d = simp(d)
    a = d[0]
    n = d[1]
    return(a*((.5)**(n)))

##This is the core loop.  This takes in a list of dyadic rationals,
##views the kth entry as the probability that there are k nemotodes
##at the start, and lets the nemotodes reproduce for n days.

def iterate(l, n = 1):
    if (n == 0):
        return(l)
    new = []
    for i in range(len(l)):
        k = i//2
        for j in range(k+1):
            if (i+j < len(new)):
                new[i+j] = plus(new[i+j], times(l[i], [math.comb(k, j), k]))
            if (i+j == len(new)):
                new.append(times(l[i],[math.comb(k, j), k]))
    return(iterate(new, n-1))

##This displays a list as above in a more human readable
##format.

def display(l):
    for i in range(len(l)):
        print(i, simp(l[i]), value(l[i]))

##This computes the expected number of nemotodes on a list.
        
def total(l):
    s = [0, 0]
    for i in range(len(l)):
        s = plus(times(dy(i), l[i]), s)
    return(simp(s))

##This is the main computational loop.  I will start with two
##nemotodes with probability 1, and run for n days.  The arrays
##that I define are for graphing, with results being the natural
##log of the results, guess1 being the predicted guess for the
##results, deltas being the deltas of results, and guess2 being
##the predicted deltas of the results.  I start with this list,
##iterate it, append the log of the total of the new list, and
##repeat.  The program will then show the graphs of results vs.
##guess1, and then deltas vs. guess2.  Guesses will be in green,
##and actual results will be in blue.  Finally, the commented
##out code shows you what the value is after i iterations and how
##it compares to (5/4)^i.

l = [[0,0], [0, 0], [1, 0]]
n = 20
results = [math.log(2)]
guess1 = [math.log((8/5))]

for i in range(n):
    l = iterate(l)
    d = total(l)
    results.append(math.log(d[0]) - d[1]*math.log(2))
    guess1.append(math.log(2) + (i * math.log(5/4)))
##    v = value(d)
##    print(2*((1.25)**(i+1)), v, v/(2*((1.25)**(i+1))))
    
deltas = []
guess2 = []
for i in range(1, len(results)):
    deltas.append(results[i]-results[i-1])
    guess2.append(math.log(1.25))

plt.plot(range(n+1), results, 'b-')
plt.plot(range(n+1), guess1, 'g-')
plt.show()
plt.cla()
plt.plot(range(1, n+1), deltas, 'b-')
plt.plot(range(1, n+1), guess2, 'g-')
plt.show()
