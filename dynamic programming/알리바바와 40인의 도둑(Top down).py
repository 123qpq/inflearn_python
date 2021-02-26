def dfs(x, y):
    if dy[x][y] > 0:
        return dy[x][y] #메모제이션 활용
    if x == 0 and y == 0:
        return table[0][0]
    else:
        if y == 0:
            dy[x][y] =  dfs(x-1, y) + table[x][y]
        elif x == 0:
            dy[x][y] = dfs(x, y-1) + table[x][y]
        else:
            dy[x][y] = min(dfs(x-1, y), dfs(x, y-1)) + table[x][y]
        return dy[x][y]

if __name__ == "__main__":
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)]
    print(dfs(n-1, n-1))