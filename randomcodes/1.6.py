a = open("C:\\Users\\VR1\\Desktop\\repository\\ura\\randomcodes\\asd.txt")
i12312123 = 0
for i in a.readlines():
    v = list(map(int,i.split()))
    d = {}
    for j in v:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
    count = 0
    g = 0
    c = 0
    count2 = 0
    for k in d:
        if d[k] == 3:
            count += 1
            c = k * 3
        elif d[k] == 1:
            g += k
            count2 += 1
    if count == 1 and count2 == 3:
        if g / 3 <= c:
            i12312123 += 1
print(i12312123)

    