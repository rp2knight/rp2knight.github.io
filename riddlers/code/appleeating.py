import random
import math
import numpy as np
import matplotlib.pyplot as plt

# This generates a random point on the sphere of radius 4.
# More specifically, this generates a random point of distance
# between 1 and 4 from the origin, and then projects it onto the
# sphere of radius 4.
def generate_point():
    while True:
        x = random.uniform(-4, 4)
        y = random.uniform(-4, 4)
        z = random.uniform(-4, 4)
        r = math.sqrt(x**2 + y**2 + z**2)
        if ((1 < r) and (r < 4)):
            return [(4*x)/r, (4*y)/r, (4*z)/r]

# This generates a mesh of points on the sphere of radius 4.
# More speciffically, this generates every point on the unit sphere
# that has two of the coordinates rational, and denominator dividing
# gap, and then scales them up to the sphere of raidus 4.
def generate_mesh(gap):
    mesh = []
    for x in range((-1)*gap, gap+1):
        b = math.floor(math.sqrt((gap**2 - x**2)))
        for y in range(-b, b+1):
            z = math.sqrt((gap**2 - x**2 - y**2))
            mesh.append([4*x/gap, 4*y/gap, 4*z/gap])
            mesh.append([4*x/gap, 4*y/gap, (-4)*z/gap])
            mesh.append([4*x/gap, 4*z/gap, 4*y/gap])
            mesh.append([4*x/gap, (-4)*z/gap, 4*y/gap])
            mesh.append([4*z/gap, 4*x/gap, 4*y/gap])
            mesh.append([(-4)*z/gap, 4*x/gap, 4*y/gap])
    return mesh

# This is the square of the distance in R^3 betwee two points on the
# sphere of radius 4 that are 1 unit apart on the sphere.
dist = 32*(1-math.cos(1/4))

# This process simulates the toddler eating an apple.  It takes a mesh
# and starts to generate random points on the sphere.  For each point it
# generates, it then removes every point in the mesh that is at most
# sqrt(dist) away from it.  It then tells you how many points needed to
# be generated to destroy the whole mesh.  k is a dummy variable that is
# only being passed in to make sure that the code is still running.  The
# print step is unnecessary but good to verify that the code is still
# running.
def simulate(mesh, k):
    count = 0
    while (len(mesh)>0):
        count += 1
        p = generate_point()
        for i in range(len(mesh)-1, -1, -1):
            d = (p[0]-mesh[i][0])**2 + (p[1]-mesh[i][1])**2 + (p[2]-mesh[i][2])**2
            if (d <= dist):
                del(mesh[i])
        if (count % 20 == 0):
            print([k, len(mesh), count])
    return count
    
# These are the main variables that need to be passed in to the main loop.
# m is the mesh that I will use.  samples is the total number of samples I
# will take.  total is the cumulative sum of all of the results I have seen.
m = generate_mesh(100)
print(len(m))
samples = 10000
total = 0

# These are variables that are used in the graphics part.  results is the list
# of results from the simulations.  maxi/mini is the maximum/minimum of the
# results.  clump is the size of the clumps that I group results into (e.g.
# if clump is 20, then any result in the interval [500, 520) is counted as the
# same for displaying things).
results = []
maxi = 0
mini = 10000
clump = 20

# This is the main loop.  I run simulate samples times, and record the results.
for i in range(samples):
    result = simulate(m.copy(), i)
    print(result)
    total += result
    results.append(result//clump)
    maxi = max(result//clump, maxi)
    mini = min(result//clump, mini)

#This is the code for displaying everything.
displayset = []
for k in range(mini, maxi+1):
    results.append(k)
    displayset.append((results.count(k)-1)/samples)

plt.plot(range(clump*mini, clump*maxi+clump, clump), displayset, 'b-')
plt.show()

print(total/samples)
