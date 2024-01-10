s = "I Love Python! Python is cool!!!"
n = 4
g = ""
for i in s:
    if i == s[n]:
        n += 4
        g += i
    if n >= len(s):
        break
print(g)
