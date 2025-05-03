with open ('26_17565 (1).txt') as file:
    N, S = map(int, file.readline().split())
    sailors = {}
    for i in file:
        sailor = list(map(int, i.split()))
        sailors[sailor[0]] = (sum(sailor[1:-1]), sailor[-1])

sailors2 = sorted(sailors, key=lambda x: (sailors[x], -x), reverse=True)

last_passed = sailors2[S - 1]
first_not_passed = sailors2[S]
if sailors[last_passed][0] == sailors[first_not_passed]:
    half_passed_point = sailors[last_passed][0]
    cnt_half_passed_point = 0
    id_full_point = 0
    for i in sailors2:
        if sailors[i][0] == half_passed_point:
            cnt_half_passed_point +=1
        if sailors[i][0] > half_passed_point:
            id_full_point = i
    print(id_full_point, cnt_half_passed_point)





























