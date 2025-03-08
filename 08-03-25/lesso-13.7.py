data = 'AAAABBBABABBBB'

for i in 'EUIIYO':
    data = data.replace(i, 'A')
print(data)
for i in 'QWRTPSDFGHJKLZXCVBNM':
    data = data.replace(i, 'B')
print(data)

while 'AA' in data or 'BB' in data:
    data = data.replace("AA", 'A A')
    data = data.replace("BB", 'B B')
data = data.split()
print(data)
ans = 0
for i in data:
    if len(i) > ans:
        ans = len(i)


print(ans)
