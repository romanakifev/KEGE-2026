# Функции
# - это обособленная группа инструкций,
# которая выполняется внутри программы и решает определённую задачу

# def <название функции>(<параметры1, параметр2, итд>):

def hello():
    print('hello')


hello()


def error(error_number):
    print('Error', error_number)


# Вызов функции с передачей значения (аргумента)
error(5)


# Значения по умолчанию
def hello_user(name='User'):
    print('Hello', name)


hello_user()
hello_user('name')


# Произвольное число аргументов
# *args - это сокращение от arguments
# позволяет передать функцию произвольное число позиционных аргументов
# * - распаковка
def calculator(*args) -> int:
    sum = 0
    for i in args:
        sum += i
    return sum


print(calculator(1, 2, 3, 11))


# **kwargs - сокращение от key word arguments
# позволяет передать функцию произвольное число именованных аргументов

def client_info(name: str, surname: str, age: int, address: str) -> None:
    '''
    Print clients data
    :param name: name of user
    :param surname: surname of user
    :param age: age of user
    :param address: address of user
    :return: None
    '''
    print('Имя клиента:', name)
    print('Имя клиента:', surname)
    print('Имя клиента:', age)
    print('Имя клиента:', address)


client1 = {'name': 'Anton', 'surname': 'Tromp', 'age': 79, 'address': 'kld'}

client_info(**client1)
