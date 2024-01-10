#(x ≡ (y → z)) ∧ (¬w → (x ≡ y))
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                a = (x == (y <= z)) and ((not(w)) <= (x == y))
                print(x, y , z ,w , a)
            #(x ≡ (y → z)) ∧ (¬w → (x ≡ y))