# Считать строку с клавиатуры.
# Найти самый часто встречающийся символ и вывести сколько раз он встречается
# и сам символ



data = input()
ans = 0
alpha = 0
for i in set(data):
    cnt = data.count(i)
    if cnt > ans:
        ans = cnt
        alpha = i
print(ans)
print(alpha)



