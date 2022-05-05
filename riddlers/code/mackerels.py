import time

##Here are a bunch of useful functions.  The first one splits
##a string into its characters.  The second one tests wheter
##two words (state and word) have no letters in common.  The
##third one takes in a word and a list of states and spits out
##all of the mackerel matches between the word and the list of
##states.  Finally, the fourth one turns a file of words into
##a list of the words in it.

def ToChars(str):
    return list(str)

def MackerelMatch(state, word):
    ret = True
    lets = ToChars(state.lower())
    letw = ToChars(word.lower())
    for i in range(len(lets)):
        for j in range(len(letw)):
            if lets[i] == letw[j]:
                ret = False
    return(ret)

def MackerelList(word, states):
    stc = len(states)
    results = []
    for i in range(stc):
        if MackerelMatch(states[i], word):
            results.append([states[i], i])
    return(results)

def WordList(file):
    f = open(file, 'r')
    output = []
    for line in f:
        length = len(line)
        output.append(line[:length-1])
    return output

##Here are some basic variables for the main loop.  states
##and words are lists of the states/words respectively, and
##are just read from files.  counts is a list of how many
##mackerels there are for a given state.  winninglength is
##the length of the winning mackerel word, winner is the
##word that won, statewinner is the state corresponding to
##the state that won, ties is a list of all the other word
##-state combos that had the same length, winningstatecounts
##is the amount of mackerels for the state with the most
##mackerels, and stateties is a list of all the states with
##the most mackerels.

states = WordList('germanstates.txt')
words = WordList('deutsch.txt')

counts = []

for i in range(len(states)):
    counts.append(0)

winninglength = 0
winner = ''
statewinner = ''
ties = []
winningstatecounts = 0
stateties = []

##This is the main loop.  It finds all mackerels and updates
##the relevant variables.

for w in words:
    l = MackerelList(w, states)
    if (len(l) == 1):
        counts[l[0][1]] += 1
        if (len(w) == winninglength):
            ties.append([w, l[0][0]])
        if (len(w) > winninglength):
            ties = []
            winninglength = len(w)
            winner = w
            statewinner = l[0][0]

##This is the display loop.  It displays all of the relevant
##information.  The drumrolls are CRUCIAL to the functioning
##of this code, and adding more is recommended if you want to
##run this code yourself.

print('And the winning mackerel is')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print('(drumroll)')
time.sleep(1)
print(winner, ', for the state of ', statewinner, '.', sep='')
if (len(ties) > 0):
    print('Congratulations to all the ties which lost the tiebreaker of alphabeticalness:')
    for i in range(len(ties)):
        print(ties[i][1], 'with a mackerel of', ties[i][0])

for i in range(len(states)):
    if (counts[i] == winningstatecounts):
        stateties.append(i)
    if (counts[i] > winningstatecounts):
        stateties = [i]
        winningstatecounts = counts[i]

if (len(stateties) == 1):
    print('The state of ', states[stateties[0]], ' had the most mackerels, with a total of ',
          winningstatecounts, ' mackerels.', sep='')
if (len(stateties) > 1):
    print('The following states all had the most mackerels, totalling', winningstatecounts)
    for i in stateties:
        print(states[i])
