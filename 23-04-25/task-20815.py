with open ('26_20815.txt') as file:
    N, K = map(int, file.readline().split())
    spacers = []
    for i in file:
        a1, a2, a3, a4, a5 = map(int, i.split())
        spacers.append([a2 + a3 + a4 + a5, a5, a1])
spacers.sort(key=lambda x: (-x[0], -x[1], x[2] ))
half_point = 0
if spacers[K-1][0] == spacers[K][0]:
    half_point = spacers[K][0]
    ans = 0
    for i in spacers:
        if i[0] == half_point:
            ans += 1
    last = 0
    for i in range(N-1):
        spacer1, spacer2 = spacers[i], spacers[i + 1]
        if spacer1[0] > spacer2[0] == half_point:
            last = spacer1[2]
    print(last)
    print(ans)
else:
    print(spacers[K-1][2], 0)

