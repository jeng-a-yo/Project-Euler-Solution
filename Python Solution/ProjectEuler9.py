import time

ST = time.time()
for m in range(1, 23):
    for n in range(1, m):
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        if a + b + c == 1000:
            print(int(a*b*c))

ET = time.time()
print(ET - ST)
