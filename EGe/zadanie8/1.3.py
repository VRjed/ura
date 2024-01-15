nol=[1]
pat=[1,8]
for i in range(1,10):
    nol.append(nol[i-1]*(10-i))
for i in range(2,10):
    pat.append(pat[i-1]*(10-i))
print(sum(pat)+sum(nol))