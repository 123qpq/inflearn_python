def dfs(i):
    global cnt
    if i == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for x in range(n):
            if check[x] == 0 and table[i-1][x] == 1:
                check[x] = 1
                path.append(x+1)
                dfs(x+1)
                path.pop()
                check[x] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    table = [[0] * n for _ in range(n)]
    check = [0] * n
    for i in range(m):
        x, y = map(int, input().split())
        table[x-1][y-1] = 1
    cnt = 0
    check[0] = 1
    path = [1]
    dfs(1)
    print(cnt)