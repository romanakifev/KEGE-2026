# Возвращает True если строка string оканчивается на suffix
#
# Если указаны параметры start/end, то suffix ищется в срезе от start до end

data = 'Hello'
print(data.endswith('Hello'))

data = input('Введите строку ')

end_line =  input("Введите на что должна оканчиваться строка")
d1 = int(input('Введите начало диапазона'))
d2 =  int(input('Введите конец диапазона'))
if d1 > d2:
    print('Начальный индекс не может быть больше конечного символа ')
elif d1 < 0 or d2 < 0:
    print('Программа принимает только положительные числа ')
elif d1 > len(data):
    print('кол-во символом d1 не должен превышать кол-во символов в строке')
else:

    if data[d1:d2][-len(end_line):] == end_line:
        print(True)
    else:
        print(False)




