import time
ST = time.time()


normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = 1901
day = 1
weekday = 1 + sum(normal_year) % 7
sum = 0

while year != 2000:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        for month_days in leap_year:
            weekday = (weekday + month_days) % 7 + 1
            if weekday == 7:
                sum += 1
        year += 1
    else:
        for month_days in normal_year:
            weekday = (weekday + month_days) % 7 + 1
            if weekday == 7:
                sum += 1
        year += 1

print(sum)

ET = time.time()
print(ET - ST)
