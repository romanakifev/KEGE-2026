data = input()

# lower() - Возвращает копию строки в нижнем регистре
print(data.lower())

# Считываем строку с клавиатуры
# Все буквы необходимо сделать маленькими
# Пример:
# Hello, HELLO, HeLlO
# hello, hello, hello

ans = ''
for i in data:
    if 'A' <= i <= 'Z':
        ans += chr(ord(i) + 32)
    else:
        ans += i

print(ans)
