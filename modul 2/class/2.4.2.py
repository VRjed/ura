a = int(input())
s = ''
for i in range(101):
    s += str(i)
    if i == a - 1:
        print(s)