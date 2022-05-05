##This is the Josephus computation.  f(k, N) gives
##the winner of the game if there are k people in
##the game and the chosen value of N is, uh, N.
def f(k, N):
    if (k == 1):
        return(1)
    return(((f(k-1, N)+N-1) % k) + 1)

##This solves the first extra credit.
print(f(61, 136232))

##This solves the second extra credit if one inteprets
##it as just the first value of N where player 1 wins.
found = False
i = 1

while(found == False):
    if(f(61, i) == 1):
        print(i)
        found = True
    i+=1

##This solves the second extra credit if one interprets
##it as the first value where the events in the problem
##transpire and player one wins.
found = False
i = 0

while(found == False):
    if(f(61, 136232+(i*61*60*59)) == 1):
        print(i, 136232+(i*61*60*59))
        found = True
    i+=1
