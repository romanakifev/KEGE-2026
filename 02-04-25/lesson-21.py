from random import randint
data = []

for i in range(20):
    data.append(randint(1, 100))
print(data)
min_el = data.index(min(data))
max_el = data.index(max(data))
if max_el > min_el:
    for i in range(min_el + 1, max_el):
        print(data[i])
else:
    for i in range(max_el +1, min_el):
        print(data[i])






