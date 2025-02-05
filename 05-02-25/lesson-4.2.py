# псевдослучайные числа
import random

# псевдослучайные число от а до b
print(random.randint(-10, 10))

# псевдослучайное число от 0 до 1
print(random.random())

# псевдослучайный элемент из списка
arr = [1, 2, 3, 4]
print(random.choice(arr))

#  n псевдослучайные элементов из списка
arr2 = [1, 2222, 3333, 5454, 65656]
n = 5
print(random.sample(arr2, n))

