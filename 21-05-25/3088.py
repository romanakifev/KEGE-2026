with open('26_3088.txt') as file:
    N = int(file.readline())
    orders = {}
    for i in file:
        time, order_id = map(int, i.split())
        if order_id not in orders:
            orders[order_id] = []
        orders[order_id].append(time)
ans2 =[]
for order_id in orders:
    orders[order_id].sort()
    middle = 0
    for i in range(0, len(orders[order_id])-1, 2):
        start, end = orders[order_id][i], orders[order_id][i+1]
        middle += end - start
        if len(orders[order_id]) > 1:
            middle /= len(orders[order_id]) // 2
        ans2.append([middle, order_id])
print(max(ans2)[1])


