from collections import deque

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
q = deque()
idx = 0
res = 0
cnt = 1
while cnt != 0:
    cnt = 0
    board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] > idx and board[i][j] == 0:
                cnt += 1
                board[i][j] = 1
                q.append((i, j))
                temp = 1
                while q:
                    now = q.popleft()
                    for a in range(4):
                        xx = now[0] + dx[a]
                        yy = now[1] + dy[a]
                        if 0 <= xx < n and 0 <= yy < n and table[xx][yy] > idx and board[xx][yy] == 0:
                            board[xx][yy] = 1
                            temp += 1
                            q.append((xx, yy))
    res = max(res, cnt)
    idx += 1
print(res)