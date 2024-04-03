alf = 'ИКЛНОР'
count = 1
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                    c = i1 + i2 + i3 + i4 
                    
                    if c.count('КИНО') == 1:
                        print(count ,' \\\\')
                        exit(1)
                    count += 1
                            