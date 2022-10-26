# Tom Schollenberger
# tss2344

# O(1)
def head(list):
    if list == []:
        return []
    else:
        return list[0]

# should be O(n)
def tail(list):
    if list == []:
        return []
    else:
        return list[1:]

# problem 1
def max2(one, two):
    return 0.5 * (abs(one - two) + abs(one + two))

# problem 2
def fSelect(list, i):
    x = head(list)
    xs = tail(list)
    l = [y for y in xs if y < x]
    s = [y for y in list if y == x]
    m = [y for y in xs if y > x]

    if i < len(l):
        return fSelect(l, i)
    elif len(l) <= i < len(l) + len(s):
        return x
    else:
        return fSelect(m, i - (len(l) + len(s)))

# problem 3
def partition(a, l, h):
    x = a[h]
    i = l - 1
    j = l
    
    while j < h:
        if a[j] < x:
            i = i + 1
            store = a[i]
            a[i] = a[j]
            a[j] = store
        j = j + 1

    store_2 = a[i + 1]
    a[i + 1] = a[h]
    a[h] = store_2

    return i + 1

def iSelectHelper(list, i, start, end):
    while True:
        m = partition(list, start, end)
        if m - start == i - 1:
            return list[m]
        else:
            if m - start > i - 1:
                end = m - 1
            else:
                i = i - m + start - 1
                start = m + 1

def iSelect(list, i):
    return iSelectHelper(list, i, 0, len(list) - 1)
