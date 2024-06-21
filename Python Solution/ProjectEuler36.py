def BinaryConvertion(number):
    return int(bin(number)[2:])


def PalindromesJudgement(number):
    return str(number) == str(number)[::-1]


list1 = []

for i in range(1, 1000001):
    if PalindromesJudgement(i) and PalindromesJudgement(BinaryConvertion(i)):
        list1.append(i)

print(list1)
print(sum(list1))
