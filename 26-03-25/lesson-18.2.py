with open('24_1874.txt') as file:
    data = file.readline()
data = data.replace('QW', 'Q W')
data = data.split()
ans = 0
cnt = 0
for i in data:
    cnt = len(i)
    if ans < cnt:
        ans = cnt
print(ans)




