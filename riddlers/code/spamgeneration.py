#!/usr/bin/python3
import random
import math
import numpy as np
import matplotlib.pyplot as plt
samples = 1000000 #total number of samples
count = 0         #total amount of spam messages across all samples
m = 0             #maximum number of spam messages across all samples
t = 100          #number of intervals each day is broken into
d = 3             #number of days
set = []          #the multiset of the number of spam messages across all samples
for test in range(samples):
    total = 1               #the total number of messages spammers can reply to in this sample
    for i in range((d*t)):  
        add = 0             #the number of new messages spammers can reply to in this time interval
        for j in range(total):
            if (random.randrange(0, t) < 1):
                add += 1    #one new message spawns in reply to a previous one with probability 1/t
        total += add
    if (test % 1000 == 0):
        print(test/1000)    #make sure the program is still chugging
    count += total - 1      
    m = max(m, total-1)
    set.append(total-1)
print(count/samples)
print(m)
displayset = []             #for graphing
displaygraph = []
for k in range(m+1):
    set.append(k)
    displayset.append((set.count(k)-1)/samples)
    displaygraph.append((math.exp(-3)*((1-math.exp(-3))**k)))
plt.plot(range(m+1),displaygraph,'b-')
plt.plot(range(m+1),displayset,'r-')
plt.show()
