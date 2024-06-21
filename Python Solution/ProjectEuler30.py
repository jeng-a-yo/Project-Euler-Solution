def digits_powers(number):
    number = str(number)
    sum = 0
    for a in range(0, len(number)):
        sum += int((number[a]))**5
    if sum == int(number):
        return True
    else:
        return False


sum = 0
for a in range(2, 1000000):
    if digits_powers(a):
        sum += a
        print(a)
print(sum)
