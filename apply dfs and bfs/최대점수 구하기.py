def dfs(l, sum, t):
    global res
    if t > time:
        return
    if l == n:
        res = max(res, sum)
    else:
        dfs(l+1, sum+solve[l][0], t+solve[l][1])
        dfs(l+1, sum, t)


if __name__ == "__main__":
    n, time = map(int, input().split())
    solve = []
    res = 0
    for _ in range(n):
        solve.append(tuple(map(int, input().split())))
    dfs(0, 0, 0)
    print(res)
