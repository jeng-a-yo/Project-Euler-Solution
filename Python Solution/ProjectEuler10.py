prime_list = [2]
for prime in range(3, 2000001, 2):
    for c in prime_list:
        if prime % c == 0:
            break
        if c ** 2 > prime:
            prime_list.append(prime)
            break
print(sum(prime_list))

# --------------------------------------------------

sum = 2

def prime(x):
    for factor in range(3, int(x ** 0.5) + 1, 2):
        if x % factor == 0:
            return False
    else:
        return True

for number in range(3, 2000001, 2):
    if prime(number):
        sum += number

print(sum)
