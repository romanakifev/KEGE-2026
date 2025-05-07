with open('26_19256.txt') as file:
    N = int(file.readline())
    students = {}
    for i in file:
        idstudent, task = map(int, i.split())
        if idstudent in students:
            students[idstudent].add(task)
        else:
            students[idstudent] = {task}
ans = []
for idstudent in students:
    tasks = sorted(students[idstudent])
    cnt = 1
    max_cnt = 0
    for i in range(len(tasks) - 1):
        if tasks[i] + 1 ==  tasks[i + 1]:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 1
    ans.append([idstudent, max_cnt])

ans.sort(key=lambda x: (-x[1], x[0]))
print(ans)





