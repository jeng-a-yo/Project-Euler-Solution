a = 1
b = 1
c = 0
d = 0

while True:
    e = (len(str(c)))
    if e == 1000:
        break
    a = b
    b = c
    c = a+b
    d += 1
print(d)
