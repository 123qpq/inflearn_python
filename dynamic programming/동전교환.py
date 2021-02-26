n = int(input())
coins = list(map(int, input().split()))
exchange = int(input())
dy = [0] + [100] * (exchange)
for coin in coins:
    for j in range(coin, exchange+1):
        dy[j] = min(dy[j], dy[j-coin]+1)
    print(dy)
print(dy[exchange])