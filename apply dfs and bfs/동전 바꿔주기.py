def dfs(l, sum):
    global cnt
    if l == n:
        if sum == pay:
            cnt += 1
    else:
        for i in range(coins[l][1]+1):
            if sum + i*coins[l][0] <= pay:
                dfs(l+1, sum + i*coins[l][0])

if __name__ == "__main__":
    pay = int(input())
    n = int(input())
    coins = []
    cnt = 0
    for _ in range(n):
        coins.append(tuple(map(int, input().split())))
    dfs(0, 0)
    print(cnt)