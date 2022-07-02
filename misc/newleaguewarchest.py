import random

def iterate_old(chest, p):
    if chest < 100:
        return([False])
    wins = 0
    for i in range(5):
        if random.random() < p:
            wins += 1
    if wins < 2:
        return([True, chest-100])
    if wins == 2:
        return([True, chest-50])
    if wins == 3:
        return([True, chest+23])
    if wins == 4:
        return([True, chest+135])
    if wins == 5:
        return([True, chest+303])

def iterate_new(chest, p):
    if chest < 100:
        return([False])
    wins = 0
    for i in range(5):
        if random.random() < p:
            wins += 1
    if wins < 2:
        return([True, chest-100, wins])
    if wins == 2:
        return([True, chest-27, wins])
    if wins == 3:
        return([True, chest+23, wins])
    if wins == 4:
        return([True, chest+112, wins])
    if wins == 5:
        return([True, chest+155, wins])

def simulate_old(start, p, succ, trials):
    busts = 0
    for t in range(trials):
        i = 0
        chest = start
        while(i<succ):
            result = iterate_old(chest, p)
            if not result[0]:
                busts += 1
                i = succ
            if result[0]:
                i += 1
                chest = result[1]
    return(busts)

def simulate_new(start, p, succ, trials):
    busts = 0
    for t in range(trials):
        i = 0
        chest = start
        while(i<succ):
            result = iterate_new(chest, p)
            if not result[0]:
                busts += 1
                i = succ
            if result[0]:
                i += 1
                chest = result[1]
    return(busts)


print(simulate_old(1000, .55, 100, 100000))
print(simulate_new(1000, .55, 100, 100000))
