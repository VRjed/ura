a = int(input())
b = int(input())
c = int(input())
v = int(input())
g = (('*'+'-'*a)*b+'*\n')
q = ((('|'+" "*a)*b+'|\n')*c)
a = ((('*'+('-'*a+ '+')*(b-1)+'-'*a+'*\n')+q)*(v-1))
print(g+q+a+g)