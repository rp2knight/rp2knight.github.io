import math
import matplotlib.pyplot as plt

def hgeom(N, K, n, k):
    return(math.comb(K, k) * math.comb(N-K, n-k)/math.comb(N, n))

xs = []
ys = []
win = 0
winner = 0

for i in range(11, 1000):
    xs.append(i)
    ys.append(hgeom(2*i, i, 19, 11))
    if hgeom(2*i, i, 19, 11) > winner:
        win = i
        winner = hgeom(2*i, i, 19, 11)

print(win, winner)

plt.plot(xs, ys, 'b.')
plt.plot([11, 999], [math.comb(19, 11)/2**19, math.comb(19, 11)/2**19], 'g-')
plt.show()
