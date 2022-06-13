import random
import matplotlib.pyplot as plt

def move(x, d=20, i=100):
    bot = max(0, x-d)
    top = min(i, x+d)
    return(random.uniform(bot, top))

def evolve(points, d=20, i=100):
    results = []
    for p in points:
        results.append(move(p, d, i))
    return(sorted(results))

def displaycounts(points, acc=200, i=100):
    loc = 1
    cdf = []
    for i in range(len(points)):
        if points[i] > loc/acc:
            cdf.append(i)
            loc += 1
    cdf.append(len(points))
    pdf = []
    for i in range(len(cdf)-1):
        pdf.append(cdf[i+1]-cdf[i])
    return(pdf)

steps = 1000

start= []
for i in range(100001):
    start.append(50)

evolution = [start]

for j in range(steps):
    evolution.append(evolve(evolution[-1]))
    print(j)

plt.hist(evolution[steps-1], 100, (0, 100), True)
plt.show()
