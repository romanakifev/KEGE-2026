# Словарь - тип коллекций, которых хранит в себе неиндексированный итерируемый
# # набор элементов в формате "ключ:значение".
# # Словари являются отдельным типом коллекций,
# # который называется отображением (mapping).
my_dict = {'name': 'Ivan', 'age': 16}
print(my_dict['name'])

# keys - все ключи словаря
print(my_dict.keys())

# values - все значения
print(my_dict.values())

# items - все связки "ключ+значения"
print(my_dict.items())

# Извлечение элемента по ключу
print(my_dict['name']) # Если ключа нет вернет ошибку
print(my_dict.get('name')) # Если ключа нет вернет None

# Удаление элементов по ключу
print(my_dict.pop('name'))
print(my_dict)

# Добавление элемента по ключу
my_dict['surname'] = 'Ivanov'
print(my_dict)



