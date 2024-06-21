def fatorial(number):
    result = 1
    for a in range(1, number+1):
        result *= a
    return result


def TF(number):
    number = str(number)
    sum = 0
    for a in range(0, len(number)):
        sum += fatorial(int(number[a]))
    if sum == int(number):
        return True
    else:
        return False


sum = 0
for a in range(3, 300001):
    if TF(a):
        sum += a
        print(a)

print(sum)
