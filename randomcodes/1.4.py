alf = 'АВЕЛРФЬ'
count = 1
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    for i6 in alf:
                        c = i1 + i2 + i3 + i4 + i5 + i6
                        count += 1
                        if (c.count('Е') == 0) and (c.count('А') == 0):
                            print(count ,' 12421')
                            exit(1)
                            