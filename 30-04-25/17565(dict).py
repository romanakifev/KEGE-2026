with open ('26_17565 (1).txt') as file:
    N, S = map(int, file.readline().split())
    sailors = {}
    for i in file:
        sailor = list(map(int, i.split()))
        sailors[sailor[0]] = sum(sailor[1:], sailor[-1])

sailors2 = sorted(sailors, key=lambda x: (sailors[x], -x), reverse=True




























