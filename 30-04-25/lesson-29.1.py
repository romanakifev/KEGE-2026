# Множество - тип коллекции, который содержит уникальные неиндексируемые элементы.
from os import remove

my_set = {1, 2, 3}

# add - добавить элемент в множество.
# можно добавлять в set - int, str, float, tuple,
# Возвращает None
my_set.add(4)
print(my_set)

# remove - удалить элемент из множества
# Возвращает None
# Возвращает None
my_set.remove(1)
print(my_set)

# discard - удаляет элемент из множества
my_set.discard(1)
# clear - очищает множество
my_set.clear()



