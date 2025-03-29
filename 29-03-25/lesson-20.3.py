# заполнить список 20-ю случайными числами в диапазоне от 1 до 100

from random import randint
data = []
for i in range(20):
    data.append(randint(-100, 100))



print(data)

minus = 0
plus = 0
for i  in data:
    if i < 0:
        minus += 1
    else:
        plus += 1


print(plus)
print(minus)