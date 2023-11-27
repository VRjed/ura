def f(x, y, n):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 2, y, n ) + f(x * 3, y, n + 1) + f(x * 5, y, n + 1)
print(f(2, 200, 0))






#def f(x, y, Flag):
  #  if x > y:
   #     return 0
  #  if x == y:
  #      return 1
  #  elif Flag:
  #      return f(x + 1, y, True) + f(x + 2, y, True) + f(x * 2, y, False)
  #  else:
  #      return f(x + 1, y, True) + f(x + 2, y, True)
#print(f(1, 9, True))







#def f(x, y, n):
 #   if x > y or n < 0:
   #     return 0
   # if x == y:
   #     return 1
   # return f(x + 1, y, n - 1) + f(x * 2, y, n - 1)
#for i in range(2, 100):
  #  if f(1, i, 5) == 0:
  #      print(i)
 #       break