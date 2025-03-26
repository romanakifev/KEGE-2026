with open('24_20813.txt') as file:
    data = file.readline()

data = data.replace ('8', '7').replace('9', '7')
data =  data.replace('-', '*')
while '**' in data:
    data = data.replace('**', '* *')
data = data.replace('*0', '* 0')
while ' 00' in data:
    data = data.replace(' 00', ' 0')
while ' 07' in data:
    data = data.replace(' 07', ' 7')
data = data.split()
ans = 0
cnt = 0
for i in data:
    i = i.strip('*')
    cnt = len(i)
    if ans < cnt:
        ans = cnt
print(ans)
