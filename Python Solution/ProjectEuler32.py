def DigitsCombination(list1):
    return "".join(list1)


def PandigitalJudgement(number):
    return sorted(list(set(number))) == [str(i) for i in range(1, 10)]


resultList = []

for number in range(1, 10000):
    for i in range(1, int(number ** 0.5)):
        if number % i == 0:
            list1 = list(map(lambda x: str(x), [i, number // i, number]))
            if PandigitalJudgement(DigitsCombination(list1)):
                resultList.append(number)
                break

print(resultList)
print(sum(resultList))
