s = "I Love Python! Python is cool!!!"
def reverse_string(variable):
    g = ''.join(reversed(variable))
    return g 
n = reverse_string(s)
print(n)