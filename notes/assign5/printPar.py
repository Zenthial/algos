import math

def extraSpace(S, M, i, j):
    sum_of_words = 0
    for k in range(i, j):
        sum_of_words += len(S[k])

    return (M - (j + i - sum_of_words))

def badnessLine(S, M, i, j):
    extra = extraSpace(S, M, i, j)
    if extra < 0:
        return math.inf
    else:
        return extra

def minBad(S, M, i):
    s = S[i]
    j = len(s)
    if i + 1 == len(S):
        return badnessLine(s, M, 0, j)
    else:
        return badnessLine(s, M, 0, j) + minBad(S, M, i + 1)

def minBadDynamic(S, M):
    n = len(S)
    tab = [0 for x in range(n)]

    for i in range(n):
        s = S[i]
        tab[i] = badnessLine(s, M, 0, len(s)) + tab[i - 1]

    return tab[n]

def minBadDynamicChoice(S, M):
    n = len(S)
    tab = [0 for x in range(n)]

    for i in range(n):
        s = S[i]
        tab[i] = badnessLine(s, M, 0, len(s)) + tab[i - 1]

    return tab[n], tab

def printParagraph(S, M):
    badness, choices = minBadDynamicChoice(S, M)
    print_str = ""
    if badness == 0:
        for s in S:
            print_str += s

    else:
        for i in range(len(S)):
            if choices[i] >= 1 and badness > 0:
                badness -= choices[i]
                print_str += S[i] + "\n"

    print(print_str)