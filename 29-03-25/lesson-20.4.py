from ipaddress import summarize_address_range
from random import randint
data = []
for i in range(20):
    data.append(randint(0, 9))
print(data)

mid = sum(data) / len(data)
print(mid)
for i in data:
    if mid > i:
        print(i)
