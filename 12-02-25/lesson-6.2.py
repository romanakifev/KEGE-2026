# Посчитать кол-во разрядов в числе
num = int(input())
cnt = 0
while  num:
    num = num // 10
    cnt += 1
print (cnt)

