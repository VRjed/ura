from itertools import product 
alphabet = '012345'
ap=[]
for i in product(alphabet, repeat=3):    
    if  i[0] != '0' and int(i[0]) >= int(i[1]) >= int(i[2]):
        ap.append(i)
print(len(ap))