def sum_of_factors(x):  # no x
    sum = 0
    for a in range(1, x):
        if x % a == 0:
            sum += a

    return sum


sum = 0

for a in range(1, 10000):
    if a == sum_of_factors(a):
        continue
    if a == sum_of_factors(sum_of_factors(a)):
        sum += a
print(sum)
