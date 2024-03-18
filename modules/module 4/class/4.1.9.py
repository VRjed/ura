a = 
def telephone(number):
    if number in a:
        if len(number) == 12:
            if number[0] == '+' and number[1] == '7':
                print('True')
            else:
                print("False")
        else:
            print("False")
    else:
        print("False")
telephone('+74954567898')
print(a)