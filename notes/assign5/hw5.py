# Tom Schollenberger
# tss2344

# problem 3
def fibDyn(n):
    tab = [0, 1];
    if n >= 2:
        for i in range(2, n+1):
            tab.insert(i, tab[i-1] + tab[i-2])
        
    return tab[n]

# problem 4b
def knapsack(pairs, capacity):
    tab = []
    
for i in range(10):
    print(fibDyn(i))