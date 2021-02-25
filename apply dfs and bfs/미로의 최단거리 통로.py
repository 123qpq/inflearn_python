from collections import deque
table = [list(map(int, input().split())) for _ in range(7)]
board = [[0]*7 for _ in range(7)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
q = deque()
q.append((0, 0))
while q:
    if board[6][6] != 0:
        break
    temp = q.popleft()
    for j in range(4):
        x = temp[0] + dx[j]
        y = temp[1] + dy[j]
        if 0 <= x < 7 and 0 <= y < 7 and table[x][y] == 0 and board[x][y] == 0:
            board[x][y] = board[temp[0]][temp[1]] + 1
            q.append((x, y))
if board[6][6] == 0:
    print(-1)
else:
    print(board[6][6])