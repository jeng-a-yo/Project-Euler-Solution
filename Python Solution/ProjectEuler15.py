def factorial(x):
    product = 1
    for a in range(1, x+1):
        product *= a
    return product


print(factorial(40)//factorial(20)//factorial(20))
