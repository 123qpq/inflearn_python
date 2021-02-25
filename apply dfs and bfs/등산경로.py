def dfs(x, y):
    global cnt
    if x == maxi // n and y == maxi % n:
        cnt += 1
        print(cnt)
        for i in board:
            print(i)
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and table[x][y]< table[xx][yy] and board[xx][yy] == 0:
                board[xx][yy] = 1
                dfs(xx, yy)
                board[xx][yy] = 0

if __name__ == "__main__":
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    lst = []
    for i in table:
        lst += i
    mini = lst.index(min(lst))
    maxi = lst.index(max(lst))
    board = [[0]*n for _ in range(n)]
    cnt = 0
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    board[mini//n][mini%n] = 1
    dfs(mini//n, mini%n)
    print(cnt)