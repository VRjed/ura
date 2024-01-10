for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = (x == (not y)) <= ((z <= (not  w)) and (w <= y))
                print(x, y , z ,w , a)




#(x ≡ ¬y) → ((z → ¬w) ∧ (w → y)).-