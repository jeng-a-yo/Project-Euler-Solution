# solution 1

import math
print(math.lcm(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
      11, 12, 13, 14, 15, 16, 17, 18, 19, 20))

import math
answer = 1  # 建立一變數為最後的結果
for number in range(2, 21):  # 建立一迴圈使一變數為一定的範圍
    answer = math.lcm(answer, number)  # 將最後結果之變數以及迴圈變數帶入函式中並更改最後結果之變數的值
print(answer) # 印出最後結果

# solution 2


def smallest_common_multiple(x, y):  # 建立一函式可找出兩數最小公倍數
    common_divisors = []  # 建立一容器來存入所有公因數
    for common_divisor in range(1, min([x, y])+1):  # 建立一迴圈為1~較小參數的自然數
        if x % common_divisor == 0 and y % common_divisor == 0:  # 判斷是否為兩參數的因數
            common_divisors.append(common_divisor)  # 條件符合將此公因數加入到容器之中
    return x*y//max(common_divisors)  # 函式回傳兩數相乘除以最大公因數


result = 1  # 建立一變數將為1~20最小公倍數
for number in range(2, 21):  # 建立一迴圈為2~20自然數
    result = smallest_common_multiple(result, number)
    # 將1~20最小公倍數之變數以及迴圈變數帶入函式中並更改1~20最小公倍數之值

print(result)  # 印出結果


# solution 3

def gcd(m, n):
    if m > n:
        return gcd(n, m)
    if n % m == 0:
        return m

    return gcd(m, n % m)


def lcm(m, n):
    return m * n / gcd(m, n)


answer = 1
for i in range(1, 21):
    answer = lcm(answer, i)
print(answer)
