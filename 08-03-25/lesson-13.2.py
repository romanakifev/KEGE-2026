# Разделение строки на подстроки при помощи разделителя ( по умолчанию пробел)
# Возвращает список подстрок
data1 = 'ivanov ivan ivanovitch'
data2 = 'ivanov.ivan.ivanovitch'
data3 = r'ivanov\u6732ivan\u6732ivanovitch '


print(data1.split())
print(data2.split('.'))
print(data3.split(r'\u6732'))
