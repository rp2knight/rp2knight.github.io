import random
import math

##This function does a simulation of a Zoom call
##with population people in it and returns the
##number of people that are in the Zoom call
##with everyone else.

def simulate(population):
    entrances = []
    exits = []
    witnesses = []
    firstexit = 1
    lastentrance = 0

    for i in range(samples):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if (y < x):
            z = y
            y = x
            x = z
        entrances.append(x)
        exits.append(y)
        if (x > lastentrance):
            lastentrance = x
        if (y < firstexit):
            firstexit = y

    for i in range(samples):
        if (entrances[i] < firstexit):
            if (exits[i] > lastentrance):
                witnesses.append(i)
    return(len(witnesses))

##These are some variables that are used for
##the simulation.  The code runs simulations
##times, and each simulation is with people
##number of people in the Zoom call.  successes
##is the number of Zoom calls with a person
##in the call with everyone else, and
##supersuccesses is the number of Zoom calls
##with at least two people in the call with
##everyone else.

simulations = 100000
people = 1000
successes = 0
supersuccesses = 0

for i in range(simulations):
    z = simulate(people)
    if (z > 0):
        successes += 1
    if (z > 1):
        supersuccesses += 1

print(successes)
print(successes/simulations)
print(supersuccesses/simulations)