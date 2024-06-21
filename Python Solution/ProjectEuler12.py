def prime_factorization(x):

    def all_factor(x):
        factors_list = []

        def factor(x):
            for b in range(2, x+1):
                if x % b == 0:
                    factors_list.append(b)
                    return factor(x//b)
        factor(x)
        return(factors_list)

    factors_dictionary = {}
    factors = all_factor(x)
    for factor in factors:
        if factor in factors_dictionary:
            continue
        times = factors.count(factor)
        factors_dictionary.update({factor: times})
    return factors_dictionary


added_number = 1
triangle_numbers = 1
number = 1


while True:
    for b in prime_factorization(triangle_numbers).values():
        number *= (b+1)
    if number > 500:
        print(triangle_numbers)
        break
    else:
        number = 1
    added_number += 1
    triangle_numbers += added_number
