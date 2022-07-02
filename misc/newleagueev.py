import matplotlib.pyplot as plt

def evpp(p):
    return([500*(p**2)*((1-p)**3) + 1000*(p**3)*((1-p)**2) + 600*(p**4)*(1-p) + 150*(p**5),
            500*(p**2)*((1-p)**3) + 1000*(p**3)*((1-p)**2) + 600*(p**4)*(1-p) + 140*(p**5)])

def evtc(p):
    return([0*(p**2)*((1-p)**3) + 10*(p**3)*((1-p)**2) + 25*(p**4)*(1-p) + 11*(p**5),
            10*(p**2)*((1-p)**3) + 10*(p**3)*((1-p)**2) + 20*(p**4)*(1-p) + 5*(p**5)])

def evqp(p):
    return(10*(p**3)*((1-p)**2) + 10*(p**4)*(1-p) + 5*(p**5))

xs = []
y1s = []
y2s = []
y3s = []
y4s = []
ys = []
z0s = []
z1s = []
z2s = []
z3s = []
z4s = []

for i in range(1001):
    p = i/1000
    xs.append(p)
    y1s.append(evpp(p)[0])
    y2s.append(evtc(p)[0])
    y3s.append(evpp(p)[1])
    y4s.append(evtc(p)[1])
    ys.append(.1*evpp(p)[0] + 2.4*evtc(p)[0] - .1*evpp(p)[1] - 2.4*evtc(p)[1])
    z0s.append(10)
    z1s.append(.1*evpp(p)[0] + 2.4*evtc(p)[0])
    z2s.append(.1*evpp(p)[1] + 2.4*evtc(p)[1])
    z3s.append(.1*evpp(p)[0] + 2.4*evtc(p)[0] + .8*evqp(p))
    z4s.append(.1*evpp(p)[1] + 2.4*evtc(p)[1] + .8*evqp(p))

plt.plot(xs, y1s, 'r-')
plt.plot(xs, y3s, 'b-')
plt.show()

plt.clf()

plt.plot(xs, y2s, 'r-')
plt.plot(xs, y4s, 'b-')
plt.show()

plt.clf()

plt.plot(xs, ys, 'g-')
plt.show()

plt.clf()

plt.plot(xs, z0s, 'g-')
plt.plot(xs, z1s, 'r-')
plt.plot(xs, z2s, 'b-')
plt.show()

plt.clf()

plt.plot(xs, z0s, 'g-')
plt.plot(xs, z3s, 'r-')
plt.plot(xs, z4s, 'b-')
plt.show()
