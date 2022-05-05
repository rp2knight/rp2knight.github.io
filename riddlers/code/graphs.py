import matplotlib.pyplot as plt

##This is the code for drawing the K7s, and telling you which
##edges cross.  The three sets of points are below; to make the
##code run, just uncomment out the set of points you wish to
##use.  Again, thanks to Oswin Aichholzer for providing the
##sets of points (and they can be found at this link:
##http://www.ist.tugraz.at/staff/aichholzer/research/rp/triangulations/crossing/)

##xs = [183, 226, 186, 125, 127, 60, 29]
##ys = [255, 45, 64, 138, 158, 74, 59]

##xs = [3, 12, 91, 52, 45, 192, 253]
##ys = [45, 210, 162, 100, 73, 132, 128]

xs = [134, 248, 180, 149, 143, 71, 8]
ys = [235, 21, 60, 149, 108, 98, 72]

##xs = [2, 253, 229, 181, 67, 84, 108, 96]
##ys = [131, 245, 223, 199, 150, 143, 66, 11]

##xs = [117, 247, 180, 158, 128, 127, 56, 8]
##ys = [181, 182, 167, 156, 170, 163, 80, 34]

##This code is used to check if the line segment connecting
##p0 to p1 and the line segment connecting q0 to q1 intersect.
##Because Oswin gives point sets that have all points in general
##position (no three points lie on the same line) I don't need to
##handle any edge cases.

def direction(p, q, r):
    val = (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
    if val < 0:
        return -1
    if val > 0:
        return 1

def intersect(p0, p1, q0, q1):
    d1 = direction(p0, p1, q0)
    d2 = direction(p0, p1, q1)
    d3 = direction(q0, q1, p0)
    d4 = direction(q0, q1, p1)
    if (d1 != d2) and (d3 != d4):
        return True
    return False

##This loop finds all pairs of line segments on the graph that
##intersect, and prints out which ones do.  As a convienent
##sanity check, for all three sets of points, there are exactly
##nine pairs of line segments that intersect.

for i in range(7):
    for j in range(i+1, 7):
        for k in range(j+1, 7):
            for l in range(k+1, 7):
                pi = [xs[i], ys[i]]
                pj = [xs[j], ys[j]]
                pk = [xs[k], ys[k]]
                pl = [xs[l], ys[l]]
                if intersect(pi, pj, pk, pl):
                    print([[i+1, j+1], [k+1, l+1]])
                if intersect(pi, pk, pj, pl):
                    print([[i+1, k+1], [j+1, l+1]])
                if intersect(pi, pl, pj, pk):
                    print([[i+1, l+1], [j+1, k+1]])

##And now, to draw the graph.  This is standard matplotlib stuff.

for i in range(7):
    for j in range(i+1, 7):
        plt.plot([xs[i], xs[j]], [ys[i], ys[j]], 'b-')

plt.plot(xs, ys, 'ro')

plt.show()
