with open('26_9077 (1).txt') as file:
    M, N = map(int, file.readline().split())
    scooters = []
    for i in file:
        scooters.append(list(map(int, i.split())))

scooters.sort()
parking = {}
timeline = [0] * 10000


for i in range(1,M+1):
    parking[i] = []
cnt = 0
for i in scooters:
    for j in range(i[0], i[0] + i[1]):
        timeline[j] += 1


    if len(parking[i[2]]) == 0:
        cnt += 1
    elif min(parking[i[2]]) > i[0]:
        cnt += 1
    else:
        parking[i[2]].remove(min(parking[i[2]]))
    parking[i[3]].append(i[0] + i[1])
print(cnt)
print(max(timeline))






