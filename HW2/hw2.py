g = 0.7
Gt = 0
for k in range(0, 50):
    Gt += g**k
    
print(Gt)

print(1 / (1 - g))
