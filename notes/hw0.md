---
id: rbjdu9xefwml3yt6jn8v1kq
title: Hw0
desc: ''
updated: 1662090305937
created: 1661904550079
---
# Tom Schollenberger (tss2344)

# Homework 0

```
Problem 1:
    s([4, 1, 3, 2]) = i(4, s([1, 3, 2]))
                    = i(4, i(1, s([3, 2])))
                    = i(4, i(1, i(3, s([2]))))
                    = i(4, i(1, i(3, i(2, s([])))))
                    = i(4, i(1, i(3, i(2, []))))
                    = i(4, i(1, i(3, [2])))
                    = i(4, i(1, 2 :: i(3, [])))
                    = i(4, i(1, [2, 3]))
                    = i(4, [1, 2, 3])
                    = 1 :: i(4, [2, 3])
                    = 1 :: 2 :: i(4, [3])
                    = 1 :: 2 :: 3 :: i(4, [])
                    = [1, 2, 3, 4]
```

```
Problem 2:
    delete(a, x :: xs) = | if x == a xs
                         | otherwise x :: delete(a, xs)

    min(x :: xs) = min(x, xs)
    min(a, x :: xs) = | if x < a min(x, xs)
                      | otherwise min(a, xs)
    min(a, []) = a

    sort(xs) = let x = min(xs)
               x :: sort(delete(x, xs))
```

```
Problem 9:
    Part 1:
        f(b, 0; a) = a
        f(b, n + 1; a) = f(b, n, a + b)

    Part 2:
        def f(b, n):
            if n = 0:
                return 1
            else:
                return f(b, n-1) * b

    Part 3:
        def f(b, n):
            result = 1
            while n != 0:
                result = result * b
                n = n - 1

            return result
```
