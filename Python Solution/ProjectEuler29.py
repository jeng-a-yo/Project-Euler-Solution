L1 = []
for a in range(2, 101):
    for b in range(2, 101):
        k = a**b
        L1.append(k)
L2 = list(set(L1))
print(len(L2))
