# все команды для работ со строками
data.replace() # первое введнное значение что заменяется, второе на что-то заменяется(заменяет любые символы)
data.strip() #  позволяет убрать лишние символы с обеих сторон строки. Также есть lstrip и rstrip r- начинает справа l-с конца
data.count() # проверят количество уникалтных символов
data.join # присоединяют одну строку к другой
end.swith # проверят на что оканчивается строка


    if ".txt" in data:
        print("Tекстовый файл")
    elif ".jpg" in data:
        print("Изображение")
    elif ".png" in data:
        print("Изображение")
    else:
        print("Неизвестный файл")


data = input()
Letters = 0
Digits = 0
for i in data:
    if i in data  == str:
        Letters += 1
    elif i in data  == int:
        Digits += 1
print(f'Цифр: {Digits}')
print(f'Букв: {Letters}')

