num1 = int(input("Введите первое пятизначное число: "))
num2 = int(input("Введите второе пятизначное число: "))
min_num = min(num1, num2)
max_num = max(num1, num2)
random_num = random.randint(min_num, max_num)
digits = [int(d) for d in str(random_num)]
- # что то должно быть.... не знаю
-
print("Сгенерированное число:", random_num)
print("Произведение цифр:", product)