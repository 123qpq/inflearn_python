def dfs(l):
    global cnt
    if l == m:
        for j in range(l):
            print(res[j], end = " ")
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] =1
                res[l] = i
                dfs(l+1)
                check[i]=0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    check = [0] * (n+1)
    cnt = 0
    dfs(0)
    print(cnt)