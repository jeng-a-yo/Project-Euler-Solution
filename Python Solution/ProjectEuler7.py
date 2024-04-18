sum = 2
number = 3
while sum < 10001:
    number += 2
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            break
    else:
        sum += 1
print(number)
