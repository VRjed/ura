a = int(input())
if a % 100 == 0:
    print("одно число")
if (a // 10 % 10 == 0 or a % 10 % 10  == 0) and a % 100 != 0:
    print("два числа")
if a > 999 or a < 100:
    print("ошибка") 
if a % 100 != 0 and a < 999 and a > 100 and a // 10 % 10 != 0 and a % 10 % 10 != 0:
    print("шесть чисел")