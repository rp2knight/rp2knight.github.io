##This function computes all possible ways to write
##n as the sum of cubes of distinct positive integers
##which are at most a.  It outputs this as a list of
##lists, the internal lists are sets of integers in
##increasing order such that the sum of the cubes of
##these integers is n.

def f(a, n):
    results = []
    if (a == 0):
        return(results)
    if (n == (a**3)):
        results.append([a])
    if (n > (a**3)):
        for l in f(a-1, n-(a**3)):
            c = l.copy()
            c.append(a)
            results.append(c)
    for l in f(a-1, n):
        c = l.copy()
        results.append(c)
    return(results)
    
##This is the main loop.  If the sum of all the cubes
##up to i is divisible by three, then it lets n be
##this sum divided by three.  Then, it calls the
##previously definied function on i and n, and gets
##a list of lists.  It then looks to see if you can
##find two lists of integers such that each integer
##from 1 to i is represented at most once, and if so
##it prints out the triple of lists.  Why 31?  This
##code is slow, and thats high enough to get the first
##solution :P (originally it was higher, but then my
##computer ran out of memory).
for i in range(31):
    if (((i % 4) == 0) or ((i % 4) == 3)):
        n = (((i+1)*i)**2)//16
        possibles = f(i, n)
        length = len(possibles)
        for j in range(length):
            for k in range(j+1, length):
                accept = True
                for m in range(1, i+1):
                    if ((possibles[j].count(m) +
                         possibles[k].count(m)) > 1):
                        accept = False
                if accept:
                    print(i, n, possibles[j], possibles[k])
