# Перенаправление потока в файл
file = open('Test.txt')
# Считывание еще не считанной строки
print(file.readline())
# Считывание еще не считанных строк
print(file.readlines())
# Закрытие потока
file.close()
