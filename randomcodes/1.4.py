def f(x, y, n):
    if x > y:
        return 0
    if x == y and n <= 3:
        return 1
    else:
        return f(x + 2, y, n )  + f(x * 3, y, n+1) + f(x * 5, y, n + 1)
print(f(2, 200, 0))