def dfs(l, start):
    global cnt
    if l == k:
        res = 0
        for x in idx:
            res += lst[x-1]
        if res % m == 0:
            cnt += 1
    else:
        for i in range(start, n+1):
            idx[l] = i
            dfs(l+1, i+1)

if __name__ == "__main__":
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    m = int(input())
    idx = [0] * k
    cnt = 0
    dfs(0, 1)
    print(cnt)