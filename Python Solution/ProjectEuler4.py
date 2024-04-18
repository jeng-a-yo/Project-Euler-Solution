answer_list = []  # 建構一容器來儲存符合的數字
for number1 in range(100, 1000):  # 建立一變數為100~999的三位數
    for number2 in range(100, 1000):  # 建立第二變數為100~999的三位數
        result_number = number1 * number2  # 將兩數相乘
        first_list = list(str(result_number))  # 將兩數相乘的結果更改為文字格式再一一分割
        opposite_list = first_list[::-1]  # 建立一新容器為「first_list」順序顛倒
        if first_list == opposite_list:  # 判斷兩容器是否相同
            answer_list.append(result_number)  # 相同說明符合條件，將此數加入道容器中儲存
print(max(answer_list))  # 印出符合條件答案中最大的數


answer_list = []  # 建構一容器來儲存符合的數字
for number1 in range(100, 1000):  # 建立一變數為100~999的三位數
    for number2 in range(number1 + 1, 1000):  # 建立第二變數為大於前一數~999的三位數
        if str(number1 * number2) == str(number1 * number2)[::-1]:  # 判斷兩文字格式逆序前後是否相同
            answer_list.append(number1 * number2)  # 相同說明符合條件，將此數加入道容器中儲存
print(max(answer_list))  # 印出符合條件答案中最大的數
