for n in range(4, 10000):
    data = '1' +'2' * n
    while '12' in data or '322' in data or '222' in data:
        if '12' in data:
            data = data.replace('12', '2', 1)
        if '322' in data:
            data = data.replace('322', '21', 1)
        if '222' in data:
            data = data.replace('222', '3', 1)
    summ = 0
    for i in data:
        summ += int(i)




