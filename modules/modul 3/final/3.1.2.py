a = int(input())
d = set()
while a != a+a:
    c = set(input().split(' '))
    a += 1
    d += c

b = list(c)
b.sort()
for i in b:
    print(i)