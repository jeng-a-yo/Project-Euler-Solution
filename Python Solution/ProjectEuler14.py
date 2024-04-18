term_dictionary = {1: 1, }

max_term = 0
answer = 0

for fixed_number in range(2, 1000000):
    number = fixed_number
    term = 0
    while number >= fixed_number:
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = 3 * number + 1
        term += 1

    final_term = term_dictionary[number] + term
    term_dictionary[fixed_number] = final_term

    if final_term > max_term:
        max_term = final_term
        answer = fixed_number

print(answer, max_term)
