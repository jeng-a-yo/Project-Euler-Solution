import time
ST = time.time()


def judge_abundant_number(number):
    sum = 0
    for a in range(1, number):
        if number % a == 0:
            sum += a

    return sum > number


abundant_number_list = []
for n in range(12, 28123+1):
    if judge_abundant_number(n):
        abundant_number_list.append(n)

# print(abundant_number_list[:20])

result = [a for a in range(1, 24)]
for a in range(25, 28123+1):
    for b in abundant_number_list:
        if b > a:
            result.append(a)
            break
        elif (a - b) in abundant_number_list:
            break
    else:
        result.append(a)


print(result)
print(sum(result))

ET = time.time()
print(ET - ST)
