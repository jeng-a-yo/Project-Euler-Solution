# solution1
first_number = 0  # 建立第一項變數為0
second_number = 1  # 建立第二項變數為1
third_number = 1  # 建立第三項變數為1
sum_of_even_value_terms = 0  # 建立一變數用來累加符合條件的值

while second_number + third_number < 4000000:  # 建立一迴圈不斷更改變數直到下一項大於400萬
    first_number = second_number  # 更改第一項為第二項
    second_number = third_number  # 更改第二項為第三項
    third_number = first_number + second_number  # 更改第三項為第一項加第二項
    if third_number % 2 == 0:  # 判斷是否為偶數
        sum_of_even_value_terms += third_number  # 若符合條件將進行累加
print(sum_of_even_value_terms)  # 印出答案

# soiution2

sum_of_even_value_terms = 0  # 建立一變數用來累加符合條件的值
first_number, second_number = 0, 1  # 同時建立第一項為0第二項為1的兩變數
while first_number + second_number < 4000000:  # 建立一迴圈不斷更改變數直到下一項大於400萬
    first_number, second_number = second_number, first_number + second_number # 將第一項與第二項同時更改為第二項與第一項加第二項
    if second_number % 2 == 0: # 判斷是否為偶數
        sum_of_even_value_terms += second_number # 若符合條件將累加
print(sum_of_even_value_terms) # 印出答案

