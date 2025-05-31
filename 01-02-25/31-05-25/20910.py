with open('26_20910.txt') as file:
    N, M, K = map(int, file.readline().split())
    free_places = [M] * (K + 1)
    for i in file:
        row, seat = map(int, i.split())
        free_places[seat] = min(row - 1, free_places[seat])

ans = []
for i in range(1, K):
    row1, row2 = free_places[i], free_places[i + 1]
    ans.append([min(row1, row2), i])
ans.sort(key=lambda x: (-x[0], x[1]))
print(ans[0])

