with open('26_4629.txt') as file:
    N = int(file.readline())
    costs = []
    for i in file:
        costs.append(int(i))
sale = N // 4
costs.sort()

cost1 = sum(costs[N - sale:]) / 2 +  sum(costs[:N - sale])
cost2 = sum(costs[:sale]) /2 + sum(costs[sale:])
print(cost1)
print(cost2)


