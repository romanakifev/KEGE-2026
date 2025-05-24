with open('26_14705.txt') as file:
    N = int(file.readline())
    exp = [list(map(int, i.split()))for i in file]
cnt = 0
ans = 0
timeline = [0] * 5_000_000
for start, end in exp:
    timeline[start] += 1
    timeline[end] -= 1
prefix_timeline = [0] * 5_000_000
prefix_timeline[0] = timeline[0]
for i in range(1, 5000000):
    prefix_timeline[i] = prefix_timeline[i - 1] + timeline[i]
max_prefix = max(prefix_timeline)
for i in range(len(prefix_timeline)):
    if prefix_timeline[i] == max_prefix:
        cnt +=1
    else:
        cnt = 0
    if cnt > ans:
        ans = cnt
print(ans)










