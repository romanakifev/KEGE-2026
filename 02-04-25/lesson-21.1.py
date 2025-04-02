from random import randint
data = []
for i in range(20):
    data.append(randint(1,100))
for i in range(20):
    if data[i] % 2 == 0:
        data[i] = 2

while 2 in data:
    data.remove(2)
print(data)


