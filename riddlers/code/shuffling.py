import random

samples = 100000000
successes = 0

deck = []

##This loop builds the deck.  It views each card
##as a number between 0 and 12 and doesn't
##distinguish between suits.
for i in range(13):
    deck.append(i)
    deck.append(i)
    deck.append(i)
    deck.append(i)

##This loop then shuffles the deck samples times,
##and sees if this shuffle will lead to a game
##where the first 26 rounds have no wars.
for i in range(samples):
    random.shuffle(deck)
    valid = True
    for j in range(26):
        if (deck[2*j] == deck[2*j+1]):
            valid = False
    if valid:
        successes += 1

print(successes, samples)
print(successes/samples, (16/17)**26)