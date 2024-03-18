count = 0
def div(x):
    if x != 0:
        count = 2
    else:
        count = 1
    if x % 2 == 0:
        count += 1
    if x % (x // 2) == 0:
        count += 1
    return count
print(div(59))

