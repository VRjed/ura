from itertools import product 
alphabet = '0123456'
ap=[]
for i in product(alphabet, repeat=4):    
    if  int(i[0]) > int(i[1]) > int(i[2])> int(i[3]):
        ap.append(i)
print(len(ap))