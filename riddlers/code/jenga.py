import random
import matplotlib.pyplot as plt

##This simulates one jenga tower being stacked and
##outputs how tall the tower was when it collapsed
##and how many blocks fell off.  Of note: it gives
##the largest number of blocks that fall off in
##case there's multiple stacks of blocks that become
##unstable.

def simulate():
    tower = []
    h = 1
    stop = False
    while(not stop):
        tower.append(random.uniform(-1, 1))
        h += 1
        for k in range(1, len(tower)+1):
            s = 0
            for i in range(k):
                s += (k-i)*tower[h-k+i-1]
            if (s > k) or (s < -k):
                stop = True
                b = k
    return([h, b])

##This simulates samples number of jenga towers.
##heights is a list of all the heights that arise,
##theight is the sum of everything in heights, and
##mheight is the largest element in heights.
##breaks, tbreak, and mbreak are the same thing
##but for how many blocks fall off.

samples = 10000000
heights = []
theight = 0
mheight = 0
breaks = []
tbreak = 0
mbreak = 0

##This is the main simulation loop.  At the end, it
##prints out the average height and the average break
##value.

for i in range(samples):
    l = simulate()
    heights.append(l[0])
    theight += l[0]
    mheight = max(mheight, l[0])
    breaks.append(l[1])
    tbreak += l[1]
    mbreak = max(mbreak, l[1])

print(theight/samples, tbreak/samples)

##This stuff is to make the pretty graph.

totheights = []
totbreaks = []

for i in range(3,mheight+1):
    totheights.append(0)

for i in range(2, mbreak+1):
    totbreaks.append(0)

for i in range(samples):
    totheights[heights[i]-3] += 1
    totbreaks[breaks[i]-2] += 1

plt.plot(range(3, mheight+1), totheights, 'b-')
plt.plot(range(2, mbreak+1), totbreaks, 'r-')
plt.show()
