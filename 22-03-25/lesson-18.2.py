data = '1' + '0' * 90

while '1' in data:
    if '10' in data:
        data = data.replace('10', '0001', 1)
    else:
        data = data.replace('1', '000', 1)
print(data.count('0'))



