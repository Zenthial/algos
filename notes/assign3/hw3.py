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

# Problem 1
def search(a, v):
    l = 0
    h = len(a) - 1
    while h >= l:
        m_hat = l + (h - l) // 2
        if v == a[m_hat]:
            return True
        elif v < a[m_hat] :
            h = m_hat - 1
        elif v > a[m_hat]:
            l = m_hat + 1

    return False

# Problem 5 (a)
def sortedHasSum(S, x):
    left_index = 0
    right_index = len(S) - 1

    while right_index >= left_index:
        sum = S[left_index] + S[right_index]
        if sum == x:
            return True
        elif sum > x:
            right_index -= 1
        elif sum < x:
            left_index += 1

    return False

# Problem 5 (b)
def hasSum(S, x):
    return sortedHasSum(sorted(S), x)

# Problem 6
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

def qs(a, l, h):
    pseudo_stack = [l, h]

    while pseudo_stack != []:
        stack_l = head(pseudo_stack)
        stack_h = head(tail(pseudo_stack))
        pseudo_stack = tail(tail(pseudo_stack))

        if stack_l < stack_h:
            m = partition(a, stack_l, stack_h)
            pseudo_stack += [m + 1, stack_h, stack_l, m - 1]

def quicksort(xs):
    return qs(xs, 0, len(xs) - 1)