a = int(input())
s = 0
for i in range(101):
    s += i
    if i == a:
        print(s)    