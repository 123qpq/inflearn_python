def dfs(x, y):
    table[x][y] = 0
    if x == 0:
        print(y)
    else:
        if y-1 >= 0 and table[x][y-1] == 1:
            dfs(x, y-1)
        elif y+1 < 10 and table[x][y+1] == 1:
            dfs(x, y+1)
        else:
            dfs(x-1, y)

if __name__ == "__main__":
    table = [list(map(int, input().split())) for _ in range(10)]
    for i in range(10):
        if table[9][i] == 2:
            dfs(9, i)
            break