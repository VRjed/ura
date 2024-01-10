def makeLevel(n):
  for i in range(1, n + 1):
    print('*'*i)
def tree(n):
  s=2
  while s!=(n+2):
    makeLevel(s)
    s+=1
n = int(input())
tree(n)