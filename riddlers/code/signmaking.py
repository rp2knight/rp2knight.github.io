import math
import scipy.integrate as integrate
import matplotlib.pyplot as plt

##This is the function f_a(x) in the writeup.  This is the
##density of ink at one spot given a gap of a.
def f(x, a):
    if ((x >= -1) and (x < a-1)):
        return(math.sqrt(1-x**2))
    if ((x >= a-1) and (x < 1)):
        return(math.sqrt(1-x**2)+math.sqrt(1-(x-a)**2))
    if ((x >= 1) and (x <= a+1)):
        return(math.sqrt(1-(x-a)**2))
    else:
        return(0)

##This gives the average amount of ink and the variance
##in amount of ink for a given value of a.
def avg(a):
    return(math.pi/(2*a))

def variance(a):
    integral = integrate.quad(lambda x: (f(x, a)-avg(a))**2, 0, a/2)
    return(integral[0]*2/a)

##These are some basic variables that are used.  accuracy
##is the inverse of the accuracy for the calculation.  xs
##and ys are for graphing things.  lowvalue is the lowest
##value of the variance, and lowpoint is the a value where
##lowvalue is attained.
accuracy = 100000
xs = []
ys = []
lowvalue = 1000
lowpoint = 0

##This is the main loop.  This just graphs the variance, and
##computes the lowest value of it.
for i in range(accuracy+1):
    x = (i/accuracy)+1
    y = variance(x)
    if (abs(y) < lowvalue):
        lowvalue = abs(y)
        lowpoint = x
    xs.append(x)
    ys.append(y)

plt.plot(xs, ys, 'r-')
plt.show()

print(lowpoint, lowvalue)

plt.close()

##This is for displaying the graph of ink density for the lowest
##variance distance.  ys is the graph of density, and avgs is
##the graph of the average amount of ink.
xs = []
ys = []
avgs = []
for i in range(accuracy+1):
    x = (i*lowpoint)/(accuracy)
    y = f(x, lowpoint)
    xs.append(x)
    ys.append(y)
    avgs.append(avg(lowpoint))

plt.plot(xs, ys, 'b-')
plt.plot(xs, avgs, 'r-')
plt.plot(0, 0, 'w.')
plt.plot(lowpoint/2, 1, 'w.')
plt.show()
