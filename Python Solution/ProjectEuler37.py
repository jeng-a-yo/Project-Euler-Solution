def spilt(number):
    all_results = []
    for a in range(1, len(str(number))):  # remove right
        all_results.append(
            int("".join(list(str(number))[:len(str(number)) - a])))

    for b in range(len(str(number))):  # remove left
        all_results.append(int("".join(list(str(number))[b:len(str(number))])))

    return all_results


def judge_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for a in range(2, int(number ** 0.5) + 1):
        if number % a == 0:
            return False
    else:
        return True


truncatable_primes_list = []
prime = 1

while not len(truncatable_primes_list) == 11:
    prime += 2
    if judge_prime(prime):
        for spilted_number in spilt(prime):
            if not judge_prime(spilted_number):
                break
        else:
            if len(str(prime)) != 1:
                truncatable_primes_list.append(prime)

print(truncatable_primes_list)
print(sum(truncatable_primes_list))
