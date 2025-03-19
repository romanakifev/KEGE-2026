data = input()
data = data.split()
ans = 0
alpha = ''

for i in data:
    i = i.rstrip('.,')
    cnt = len(i)
    if '.' in i or ',' in i:
        cnt -=1
    if cnt > ans:
        ans = cnt
        alpha = i


print(ans)
print(alpha)

