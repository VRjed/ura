a = input()
alphabet = {
    "a": "Alpha", "b": "Bravo", "c": "Charlie", "d": "Delta", "e": "Echo",
    "f": "Foxtrot", "g": "Golf", "h": "Hotel", "i": "India", "j": "Juliett",
    "k": "Kilo", "l": "Lima", "m": "Mike", "n": "November", "o": "Oscar",
    "p": "Papa", "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango",
    "u": "Uniform", "v": "Victor", "w": "Whiskey", "x": "Xray", "y": "Yankee",
    "z": "Zulu"
}
b = ''
for i in range(26):
    b += chr(ord('a') + i)
print(b)
for i in a:
    j = i
    c = '"' + i + '"'
    if j in b:

        d = alphabet.get(c,'')
        print(c)
        g = d + ' '
        print(g)
    else:
        continue
print(d)
#Py6!54th!o6657n