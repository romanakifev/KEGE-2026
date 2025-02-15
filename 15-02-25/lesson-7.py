num = int(input())
summ = 0
while num > 0:
    if num % 10 % 2  == 1:
        summ += (num % 10) ** 3
    else:
        summ += (num % 10) ** 2
    num = num // 10

print(summ)




