def dfs(l, sum, time):
    global res
    if l == n:
        res = max(res, sum)
    else:
        if time + test[l][1] <= m:
            dfs(l+1, sum + test[l][0], time + test[l][1])
        dfs(l+1, sum, time)

if __name__ == "__main__":
    n, m = map(int, input().split())
    test = [tuple(map(int, input().split())) for _ in range(n)]
    res = 0
    dfs(0, 0, 0)
    print(res)