# def changed_prime(x):
#     return int(str(prime)[1:]+str(prime)[0])

PRIME_LIST = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 197]
for number in range(3, 1000000):
    for prime_list_number in PRIME_LIST:
        if number % prime_list_number == 0:
            break
    else:
        PRIME_LIST.append(number)

print("length of PRIME_LIST", len(PRIME_LIST))
circular_prime_list = []


for prime in PRIME_LIST:
    true_times = 0
    changed_prime = str(prime)[1:]+str(prime)[0]
    for times in range(1, len(str(prime))):
        if int(changed_prime) in PRIME_LIST:
            true_times += 1
        changed_prime = str(changed_prime)[1:]+str(changed_prime)[0]
    if true_times == len(str(prime)) - 1:
        circular_prime_list.append(prime)


print(len(circular_prime_list))
