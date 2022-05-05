##This generates a list of all predictions for a best of
##n series, where you predict a team wins or loses.
def genPredict(n):
    work = [[]]
    out = []
    while(True):
        if (len(work) == 0):
            return(out)
        seq = work.pop()
        if (len(seq) < n):
            seq1 = seq.copy()
            seq1.append('w')
            seq2 = seq.copy()
            seq2.append('l')
            work.append(seq1)
            work.append(seq2)
        if (len(seq) == n):
            out.append(seq)

##This generates a list of all possible results in a best of
##2n-1 series, with the same notation as above.
def genResult(n):
    work = [[]]
    out = []
    while(True):
        if (len(work) == 0):
            return(out)
        seq = work.pop()
        if ((seq.count('w') == n) or (seq.count('l') == n)):
            out.append(seq)
        if ((seq.count('w') < n) and (seq.count('l') < n)):
            seq1 = seq.copy()
            seq1.append('w')
            seq2 = seq.copy()
            seq2.append('l')
            work.append(seq1)
            work.append(seq2)

##This computes how many games a given prediction gets right
##on a given result.  This assumes len(predict) >= len(result).
def score(result, predict):
    score = 0
    for i in range(len(result)):
        if (result[i] == predict[i]):
            score += 1
    return(score)

##This couptes how likely a prediction is to get at least goal
##games right in a collection of results.  Again, this assumes
##that len(predict) >= len(results[i]) for all i.
def success(results, predict, goal):
    p = 0
    for i in range(len(results)):
        if (score(results[i], predict) >= goal):
            p += 2**((-1)*len(results[i]))
    return(p)

##This finds all the best predictions for a series of length
##2*series - 1 and outputs the odds of winning as well as all
##the best predictions.
def findWinners(series, goal):
    predicts = genPredict(2*series - 1)
    results = genResult(series)
    win = 0
    winners = []
    for i in range(len(predicts)):
        p = success(results, predicts[i], goal)
        if (p == win):
            winners.append(predicts[i])
        if (p > win):
            win = p
            winners = [predicts[i]]
    return([win, winners])

##This is where you tweak inputs and outputs.
print(findWinners(4, 2))
        
