import random
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
# sqrt(dist) away from it.  It then outputs a list of the points that
# were needed to eat the apple.
def simulate(mesh):
    count = 0
    points = []
    while (len(mesh)>0):
        count += 1
        p = generate_point()
        points.append(p)
        for i in range(len(mesh)-1, -1, -1):
            d = (p[0]-mesh[i][0])**2 + (p[1]-mesh[i][1])**2 + (p[2]-mesh[i][2])**2
            if (d <= dist):
                del(mesh[i])
        if (count % 20 == 0):
            print([len(mesh), count])
    print(count)
    return points

# The next few processes are for drawing the circles needed to display the
# apple being eaten.  Ultimately, the final process takes in a point on the
# sphere of radius 4 and outputs three arrays needed for pyplot to show the
# the corresponding circle.
def newvect1(point):
    x = point[0]
    y = point[1]
    z = point[2]
    r = math.sqrt(x**2 + y**2)
    if (r > 0):
        z1 = z*math.cos(1/4) - r*math.sin(1/4)
        r1 = r*math.cos(1/4) + z*math.sin(1/4)
        x1 = (r1*x)/r
        y1 = (r1*y)/r
        return [x1-x, y1-y, z1-z]
    else:
        return [4*math.sin(1/4), 0.0, 0.0]

def newvect2(points):
    x0 = points[0][0]
    y0 = points[0][1]
    z0 = points[0][2]
    x1 = points[1][0]
    y1 = points[1][1]
    z1 = points[1][2]
    x2 = (y0*z1)-(y1*z0)
    y2 = (z0*x1)-(z1*x0)
    z2 = (x0*y1)-(x1*y0)
    r1 = math.sqrt(x1**2 + y1**2 + z1**2)
    r2 = math.sqrt(x2**2 + y2**2 + z2**2)
    return [(r1*x2)/r2, (r1*y2)/r2, (r1*z2)/r2]

def circle(point):
    p2 = newvect1(point)
    p3 = newvect2([point, p2])
    x1 = point[0]*math.cos(1/4)
    y1 = point[1]*math.cos(1/4)
    z1 = point[2]*math.cos(1/4)
    x2 = p2[0]
    y2 = p2[1]
    z2 = p2[2]
    x3 = p3[0]
    y3 = p3[1]
    z3 = p3[2]
    xvals = []
    yvals = []
    zvals = []
    for i in range(201):
        xvals.append(x1 + x2*math.cos((np.pi*i)/100) + x3*math.sin((np.pi*i)/100))
        yvals.append(y1 + y2*math.cos((np.pi*i)/100) + y3*math.sin((np.pi*i)/100))
        zvals.append(z1 + z2*math.cos((np.pi*i)/100) + z3*math.sin((np.pi*i)/100))
    return [xvals, yvals, zvals]

# This is the main drawing part.  The extra points in the figure are to keep
# the dimensions of the figure constant across all of the images.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
pointset = simulate(generate_mesh(50))

xs = [5, -5]
ys = [5, -5]
zs = [5, -5]

# This loop puts all the points into the scatter plot.  Additionally, this
# creates a figure for each point in the pointset.  This figure has all the
# points up to the one that just got added in, as well as the circle around
# that point.  This figure isn't displayed but rather saved to the file
# slideshow(n).png.
for i in range(len(pointset)):
    ax = fig.add_subplot(111, projection='3d')
    xs.append(pointset[i][0])
    ys.append(pointset[i][1])
    zs.append(pointset[i][2])
    circ = circle(pointset[i])
    ax.plot(circ[0], circ[1], circ[2])
    ax.scatter(xs, ys, zs)
    s = 'slideshow' + str(i) + '.png'
    plt.savefig(s)
    plt.clf()

# Finally, we show the final scatterplot.
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xs, ys, zs)

plt.show()
