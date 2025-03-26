data =  '9' * 100
while '33333' in data or '999' in data :
    if '33333' in data:
        data = data.replace('33333', '99',1)
    else:
        data = data.replace('999','3', 1)
print(data)

