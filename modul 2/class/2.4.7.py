n = int(input())
n = n - 1
sim = input()
g = str(sim)
c = 1
for i in range (n):
    while 1 <= c <= n:
        c += 1
        g +=  2 * str(sim)
        print(g)