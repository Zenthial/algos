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

# problem 5
# starts showing signs of slowing down around 30
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# problem 7
# exceeds maximum recursion depth before slowing down
def fibItHelper(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibItHelper(n - 1, b, a + b)

def fibIt(n):
    return fibItHelper(n, 0, 1)

