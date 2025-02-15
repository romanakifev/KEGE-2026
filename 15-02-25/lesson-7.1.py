num = int(input())

summ = 0
mult = 1
while num > 0:
    if num % 10 % 2  == 1:
        summ += (num % 10)
    elif num % 10 > 0:
        mult *= (num % 10)
    num = num // 10

if summ == 0:
    print('не было нечетных цифр')
else:
    print('сумма равна', summ)

if mult == 1:
    print('не было четных цифр')
else:
    print('произведение', mult)



