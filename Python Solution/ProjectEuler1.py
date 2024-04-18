print(sum([number for number in range(1, 1000)
      if number % 3 == 0 or number % 5 == 0]))


sum_of_multiples = 0  # 建立一變數用來計算符合條件倍數之和
for number in range(1, 1000):  # 建立「number」變數為1000以下自然數
    if number % 3 == 0 or number % 5 == 0:  # 判斷變數是否為3或5的倍數
        sum_of_multiples += number  # 若是3或5的倍數將此變數進行累加
print(sum_of_multiples)  # 印出最後的結果
