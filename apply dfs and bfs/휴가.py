def dfs(l, pay):
    global res
    if l == n:
        res = max(res, pay)
    else:
        if l+plan[l][0] <= n:
            dfs(l+plan[l][0], pay + plan[l][1])
        dfs(l+1, pay)

if __name__ == "__main__":
    n = int(input())
    plan = []
    res = 0
    for _ in range(n):
        plan.append(tuple(map(int, input().split())))
    dfs(0, 0)
    print(res)