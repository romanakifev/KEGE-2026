# Алгоритм перевода в любую систему исчисления (2 <= sys <= 9)
num = int(input()) # введение числа с клавиатуры
sys = int(input()) # введение системы исчисления с клавиатуры

res = '' # введение переменной строки
while num != 0: # пока num не равно 0 (сравнение с нулем после каждого действия)
    res += str (num % sys) # деление с остатком num на sys
    num = num // sys # деление на сус что бы был цикл ( не бесконечный )

print(res[::-1]) # выводим res и переворачиваем строку


