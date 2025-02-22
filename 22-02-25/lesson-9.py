data0 = [1, 2, 3]
data2 = 'hello'
data3 = {1, 2, 6, 7}
data4 = {'name': 'ivan', }


data = input()

for i in range(-1, len(data) * (-1) - 1, -1):
    print(data[i])

    print()

for i in range(1, len(data)+1):
    print(data[-i])
    
