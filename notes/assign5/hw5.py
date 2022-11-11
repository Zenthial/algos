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
    n = len(pairs)
    tab = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                tab[i][w] = 0
            else:
                weight, value = pairs[i-1] 
                if weight <= w:
                    tab[i][w] = max(value + tab[i-1][w-weight], tab[i-1][w])
                else:
                    tab[i][w] = tab[i-1][w]
 
    return tab[n][capacity]

def knapsackContents(pairs, capacity):
    n = len(pairs)
    tab = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                tab[i][w] = 0
            else:
                weight, value = pairs[i-1] 
                if weight <= w:
                    tab[i][w] = max(value + tab[i-1][w-weight], tab[i-1][w])
                else:
                    tab[i][w] = tab[i-1][w]

    totalValue = tab[n][capacity]
    items = []

    for i in range(n, 0, -1):
        if totalValue <= 0:
            break

        if totalValue == tab[i - 1][capacity]:
            continue
        else:
            weight, value = pairs[i-1]
            items += [value]
                
            totalValue = totalValue - value
            capacity = capacity - weight

    return items
    
for i in range(10):
    print(fibDyn(i))