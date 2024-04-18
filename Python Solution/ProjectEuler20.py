factorial = 1
sum = 0
for a in range(1, 101):
    factorial *= a
for b in str(factorial):
    sum += int(b)
print(sum)

