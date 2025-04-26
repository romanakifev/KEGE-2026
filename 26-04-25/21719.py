with open ('26_21719.txt')as file:
    N = int(file.readline())
    students = []
    for i in file:
        students.append(list(map(int, i.split())))

students.sort()

cnt = 1
ans = []
for i in range(N - 1):
    student1, student2 = students[i], students[i + 1]
    if student1[0] == student2[0]:
        if student1[1] == student2[1]:
            continue
        if student2[1] - student1[1] == 2:
            cnt += 1
        else:
            cnt = 1
    else:
        cnt = 1

    ans.append([cnt, student1[0]])
ans.sort(key=lambda x: (x[0], -x[1]))
print(ans)





















































































































