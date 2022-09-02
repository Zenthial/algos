# Tom Schollenberger (tss2344)

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

# problem 3
def r(list):
    if list == []:
        return []
    else:
        reversed = r(tail(list))
        reversed.append(head(list))
        return reversed

# problem 4
def prod(m, n):
    if m == 0:
        return 0
    else:
        return prod(m - 1, n) + n

# problem 5
def fastPow(b, k):
    if k == 0:
        return 1
    else:
        return fastPow(b, k - 1) * b

# problem 6
def prodAccum(m, n, a):
    if m == 0:
        return a
    else:
        return prodAccum(m - 1, n, n + a)

# problem 7
def fallibleAddition(a: int | None, b: int | None) -> int | None:
    if a != None and b != None:
        return a + b
    else:
        return None

def min(a: int | None, b: int | None) -> int | None:
    if a != None and b == None:
        return a
    elif a == None and b != None:
        return b
    else:
        return None

def minChange(a, list):
    if a == 0:
        return 0
    elif list == []:
        return None
    else:
        d = head(list)
        if d > a:
            return minChange(a, tail(list))
        else:
            return min(fallibleAddition(1, minChange(a - d, list), minChange(a, tail(list))))

# problem 8
def quotient(a, b):
    if a != None and b != None:
        return a // b
    else:
        return None

def remainder(a, b):
    if a != None and b != None:
        return a % b
    else:
        return None

def greedyMinChange(a, list):
    if a == 0:
        return 0
    elif list == []:
        return None
    else:
        d = head(list)
        if d > a:
            return greedyMinChange(a, tail(list))
        else:
            q = quotient(a, d)
            r = remainder(a, d)
            return fallibleAddition(q, minChange(r, tail(list)))

# problem 9
def powIt(b, n):
    result = 1
    while n != 0:
        result = result * b
        n = n - 1

    return result