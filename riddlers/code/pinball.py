import math

## This computes the intersection point on the
##circle given that your initial point is at x
##and your slope is m.
def intersection(x, m):
    a = 1+m*m
    b = 2*m*(x-2*m)
    c = (x-2*m)**2-1
    ynew =(-b+math.sqrt(b*b-4*a*c))/(2*a)
    xnew = m*(ynew-2) + x
    return [xnew, ynew]

##This computes the next pair of x and m from
##your current pair.
def nextpoint(x, m):
    v = intersection(x, m)
    n = v[0]/v[1]
    mnew = ((2*n-m+m*n*n)/(1+2*m*n-n*n))
    dy = 2-v[1]
    xnew = v[0]+dy*mnew
    return [xnew, -1*mnew]

##This just iterates the previous function k times.
def iterate(x, m, k):
    if (k == 0):
        return[x, m]
    v = nextpoint(x, m)
    return iterate(v[0], v[1], k-1)

##This is the function that we are looking for a zero
##of.
def f(x, k):
    m = 1-(x/2)
    v = iterate(x, m, k)
    return v[0]-math.sqrt(2)*v[1]

##These two functions approximate a zero of f by doing
##midpoint division.
def nextpair(a, b, n):
    y1 = f(a, n)
    y2 = f((a+b)/2, n)
    y3 = f(b, n)
    if (y1/y2 > 0):
        return([(a+b)/2, b])
    if (y2/y3 > 0):
        return([a, (a+b)/2])

def approximate(a, b, n, k):
    if (k == 0):
        return (a+b)/2
    v = nextpair(a, b, n)
    return approximate(v[0], v[1], n, k-1)

print(approximate(.82, .83, 0, 40))
print(approximate(.82, .83, 1, 40))
print(approximate(.82, .83, 2, 40))
print(approximate(.82, .83, 3, 40))
print(approximate(.82, .825, 4, 40))
