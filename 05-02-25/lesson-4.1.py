 # подключение библиотеки
import random
print(random.randint(1, 10))

# подключение библиотеки через псевдоним
import random as biblia
print(biblia.randint(-20,-20))
from random import randint

# подключение одной команды (randint)  из библиотеки
print(randint(-100, 100))

#подключение всех команд из библиотеки
from random import *
print(randint(-100, 100))


