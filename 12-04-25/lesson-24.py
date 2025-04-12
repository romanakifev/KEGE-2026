with open('26_954.txt') as file: #№ 954 (Уровень: Базовый)
    N, K, M = map(int, file.readline().split())
    prices =[]
    for i in file:
        prices.append(int(i))
prices.sort()
max_price = prices[-100:]
max_sale = sum(max_price) * 0.2
min_price = prices[-250:-100]
min_sale = sum(min_price) * 0.1
ans = min_sale + max_sale
print(ans)
max_cena = prices[-251]
print(max_cena)







