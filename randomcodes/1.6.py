from random import randint
n = int(input())                                                                      
a = [randint(0,100) for i in range (n)]
max = a[0]
min = a[0]
print (a)
for i in range(n-1):
    if a[i] < min:
        min = a[i]
    else:
        if a[i] > max:
            max = a[i]
print (min,max)