a = '123456789+'
b = 'True'
def telephone(number):
    for i in number:
        if i in a:
            continue
        else:
            b = "False"
    if b == 'True':
        if len(number) == 12:
            if number[0] == '+' and number[1] == '7':
                b = 'True'
            else:
                b = "False"
        else:
            b = "False"
        print(b)     
    else:
        print(b)
telephone('+7914034630a')