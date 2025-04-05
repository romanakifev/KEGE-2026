# Взаимодействие файлом с автоматическим закрытием потока
with open('Test.txt') as file:
    data = file.readline()
print(data)
