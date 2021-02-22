def dfs(l, sum):
    global res
    if sum > exchange or l > res:
        return
    if sum == exchange:
            if l < res:
                res = l
    else:
        for coin in coins:
            dfs(l+1, sum+coin)

if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort(reverse = True)
    exchange = int(input())
    res = float('inf')
    dfs(0, 0)
    print(res)