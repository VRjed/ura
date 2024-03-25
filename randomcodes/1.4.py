def f(n):
    c = bin(n)[2:]
    a = c.count("1")
    if a % 2 == 0:
        c ="10" + c[2:] + '1'
    else:
        c = "1" + c[2:] + '11'  
    return int(c,2)
for n in range(1, 100000):
    if f(n) > 100:
        print(n)
        break