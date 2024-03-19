f = 0
def factorial(n):
    if n <= 1:
        return 1
    f = factorial(n-1) * n
    return f 
print(factorial(7))