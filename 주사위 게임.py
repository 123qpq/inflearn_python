n = int(input())
res = 0
for _ in range(n):
    dice = list(map(int, input().split()))
    dice.sort()
    if dice[0] == dice[2]:
        money = 10000 + dice[0] * 1000
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        money = 1000 + dice[2] * 100
    else:
        money = dice[2] * 100
    if money > res:
        res = money
print(res)
