def dfs(l):
    global cnt
    if l == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            res[l] = i
            dfs(l+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0 for _ in range(m)]
    cnt = 0
    dfs(0)
    print(cnt)