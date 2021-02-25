def dfs(x, y):
    global cnt
    cnt += 1
    table[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and table[xx][yy] == 1:
            dfs(xx, yy)

if __name__ == "__main__":
    n = int(input())
    table = [list(map(int, input())) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    res = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                cnt = 0
                dfs(i, j)
                res.append(cnt)

    print(len(res))
    for i in sorted(res):
        print(i)