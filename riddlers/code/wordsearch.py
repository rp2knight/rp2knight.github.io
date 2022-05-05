import math
import matplotlib.pyplot as plt

def g(n):
    if (n == 1):
        return(1)
    if (n == 2):
        return(3)
    if ((n%2) == 1):
        return(n + 2*g((n-1)//2))
    if ((n%2) == 0):
        return(n + g(n//2) + g((n//2)-1))
gvals = [0,1]
for i in range(1, 2**19):
    gvals.append(2*i + gvals[i] + gvals[i-1])
    gvals.append(2*i+1+2*gvals[i])
    
print(g(267751))
yvals = []
xvals = []

for i in range(2**0, 2**20):
    xvals.append(math.log2(i))
    yvals.append(math.log2(i)-(gvals[i]/i))

plt.plot(xvals, yvals, 'b-')
plt.plot(9, 0, 'w.')
plt.show()
