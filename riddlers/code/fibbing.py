##target is the number that is trying to be encoded.
##best is the best value of q.  winning is the best
##triple (a, b, q)

target = 81
best = 0
winning = []

##This code just loops over all possibilities of a and b
##and looks for ones that hit q.  If it finds a hit, it
##checks to see if this is a better hit and if so updates
##best and winning.

for a in range(1, target):
    for b in range(1, target):
        x = a
        y = b
        q = 0
        while(y < target):
            z = x
            x = y
            y = z + y
            q += 1
        if y == target:
            if q > best:
                best = q
                winning = [a, b, q]

print(target, winning)
