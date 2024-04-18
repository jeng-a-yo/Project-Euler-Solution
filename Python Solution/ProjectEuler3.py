# solution1
def juagment(x):  # 質數判斷函式
    if x == 1:  # 1不為質數
        return False  # 回傳布林值「False」
    elif x == 2:  # 2為質數
        return True  # 回傳布林值「True」
    for test_number in range(2, x):
        if x % test_number == 0:
            return False  # 回傳布林值「False」
    else:  # 沒有檢測到可以整除的樹
        return True  # 回傳布林值「True」


question_number = 600851475143  # 題目數字
prime_factor = 0  # 要檢測的因數

for prime_factor in range(2, question_number):  # 建立一變數會為題目數字以下所有的自然數
    if question_number % prime_factor == 0 and juagment(prime_factor): # 判斷是否為因數同時又為質數
        question_number /= prime_factor  # 將題目的數字更改為題目的數字除以此質因數
        if question_number % prime_factor == 0:  # 判斷是否為此質因數多次方
            while question_number % prime_factor == 0:  # 直到無此質因數
                question_number /= prime_factor  # 將次方全部除去
print(prime_factor)  # 印出最後的質數

# solution2


def all_factor(x): # 建立一函式用來回傳所有質因數
    def factor(x): # 建立一函式用來執行質因數分解
        for test_number in range(2, x+1): # 設一變數為題目之數以下的自然數
            if x % test_number == 0: # 判斷題目之數是否可以被此變數整除
                factors_list.append(test_number) # 將此數存入一容器之中
                return factor(x//test_number) # 回傳此函數更改參數為題目之數除以此變數
    factors_list = [] # 建立一容器(列表)
    factor(x) # 呼叫「factor」函式對參數進行質因數分解
    return(factors_list) # 回傳質因數分解結果
    
print(max(all_factor(600851475143))) # 運用「max()」函式找出最大值因數並印出


