n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
board = [[0]* (n) for _ in range(n)]
board[0][0] = table[0][0]
for i in range(1, n):
    board[i][0] = board[i-1][0] + table[i][0]
    board[0][i] = board[0][i-1] + table[0][i]
    
for x in range(1, n):
    for y in range(1, n):
        board[x][y] = table[x][y] + min(board[x][y-1], board[x-1][y])

print(board[n-1][n-1])