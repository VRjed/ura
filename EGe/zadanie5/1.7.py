def R(n): # описываем наш алгоритм
    s = bin(n)[2:] # строим двоичную запись
    if n % 2 == 0:
        s = s + '10'
    else:
        s = s + '01'
   

    return int(s, 2) # переводим полученное число в десятичную систему счисления
for n in range(1, 10000): # перебираем все возможные значения N
    if R(n) > 150: # если полученное значение R превышает 1038
        print(R(n)) # выводим первое найденное значение 
        break # выходим из цикла
print('|//end//|')