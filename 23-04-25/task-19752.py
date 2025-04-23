with open ('26_19752.txt') as file:
    N = int(file.readline())
    players = []
    for i in file:
        data = list(map(int, i.split()))
        summ = sum(data[1:])
        plus = sum([j for j in data[1:] if j > 0])
        ans = 10 - data[1:].count(0)
        players.append([data[0], summ, plus, ans])

players.sort(key=lambda x:(-x[1], -x[2], -x[3], x[0]))
print(players[:100])
cnt_winners = 0
for player in players[N // 3:]:
    if players[N // 3 - 1][1:] == player[1:]:
        cnt_winners += 1
    players = players[N // 3 + cnt_winners:]
id_winner = players[0]
cnt_losers = 0
half_losers = []
for player in players[:len(players) // 10]:
    if player[1] > 0:
        half_losers.append(player)
for player in players[len(players) // 10:]:
    if half_losers[-1][1:] == player[1:]:
        half_losers.append(player)
print(id_winner, len(half_losers))



