s = "I Love Python! Python is cool!!!"
n = 4
for i in s:
    if i == s[n]:
        n += 4
        print (i)
    if n >= len(s):
        break