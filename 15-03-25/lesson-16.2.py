data = 'ababbbab abababa baacacacaca'
delete = 'ab'
res = ''
for i in data:
    if i not in delete:
        res += i
print(res)

for i in delete:
    data = data.replace(i , '')

print(data)

data = 'ababbabbbbbbbbbbabababcccc'
delete= 'b'
for i in delete:
    data = data.split(i)
    data = ''.join(data)


