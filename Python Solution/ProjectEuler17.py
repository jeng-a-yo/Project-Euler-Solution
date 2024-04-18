from num2words import num2words

sum = 0
for number in range(1, 1001):
    sum += (len(''.join(''.join(num2words(number).split('-')).split(' '))))


print(sum)
