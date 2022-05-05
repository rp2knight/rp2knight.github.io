import random

##This code plays a single game, with a deck consisting
##of the cards between 1 and n, as well as one joker.
##It takes the strategy of drawing if and only if that
##increases it's score.

def play(n):
    deck = ['J']
    high = 0
    for i in range(n):
        deck.append(i+1)
        high += i+1
    score = 0
    while(2*score < high):
        random.shuffle(deck)
        card = deck.pop()
        if card == 'J':
            return(0)
        score += card
    return(score)

##This simulates playing the game samples times with a
##deck that consists of the cards between 1 and n and one
##joker.  It prints out the average score and the number
##of times a joker is drawn.

def simulate(n, samples):
    totscore = 0
    jokes = 0
    for i in range(samples):
        s = play(n)
        totscore += s
        if s == 0:
            jokes += 1
    print(totscore/samples, jokes/samples)

simulate(10, 1000000)
