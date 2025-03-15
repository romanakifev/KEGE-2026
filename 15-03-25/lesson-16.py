data = 'ABABABAAAABBABABAB'
data = data.replace('A', '*').replace('B', '*')
data = data.replace('1', '#').replace('2', '#')
data = data.replace('*#', '3')

data = data.replace('*', ' ')
data = data.replace('#', ' ')

data = data.split()
ans = 0

for i in data:
    ans = max(len(i), ans)

print(ans)

data = 'AA12B1B1ABABAAAAAABBB2B1'
cnt = 0
for i in range(len(data) -1 ):
    l1, l2 = data[i], data[i + 1]
    if l1 in 'AB' and l2 in '12':
        cnt += 1





