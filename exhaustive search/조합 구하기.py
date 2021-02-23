def dfs(l, start):
    global cnt
    if l == m:
        for x in res:
            print(x, end=" ")
        print()
        cnt += 1
    else:
        for i in range(start, n+1):
            res[l] = i
            dfs(l+1, i+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    dfs(0, 1)
    print(cnt)