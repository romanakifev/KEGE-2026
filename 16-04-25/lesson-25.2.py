with open('26_7274.txt') as file:
     N =  int(file.readline())
     trees = []
     for i in file:
        row, col = map(int, i.split())
        trees.append([row, col])
trees.sort()
ans = []
for i in range(N - 1):
    tree1, tree2 = trees[i], trees[i + 1]
    if tree1[0] == tree2[0] and tree2[1] - tree1[1] - 1 == 13:
        ans.append([tree1[0], tree1[1] + 1])
print(ans)