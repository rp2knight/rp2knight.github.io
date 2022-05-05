import math

##This computes the values of p(n) up to top, with
##values being the, well, values.

values = [0, 1]
top = 1000

for n in range(2, top):
    s = 0
    for k in range(n):
        s += values[k]*math.comb(n, k)/(2**n-1)
    values.append(s)

print(values)
