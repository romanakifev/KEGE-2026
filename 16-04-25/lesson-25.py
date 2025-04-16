with open('../12-04-25/26.2_19727.txt') as file: #№ 19772 (Уровень: Базовый)
    M, N = map(int, file.readline().split())
    litr = []
    for i in file:
        litr.append(int(i))
litr.sort()
min_litr = 0
cnt = 0
for i in litr:
    if M >= min_litr + i:
        min_litr += i
        cnt += 1
cnt2 = 0
for i in litr:
    if sum(litr[:cnt-1]) + i > M:
        cnt2 += 1
print(cnt, cnt2)













