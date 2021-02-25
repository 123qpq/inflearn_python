from collections import deque

n = int(input())
table = [list(map(int, input())) for _ in range(n)]
board = [[0]*n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
q = deque()
cnt = 0
res = []
for i in range(n):
    for j in range(n):
        if table[i][j] == 1 and board[i][j] == 0:
            cnt += 1
            board[i][j] = cnt
            q.append((i, j))
            temp = 1
            while q:
                now = q.popleft()
                for a in range(4):
                    xx = now[0] + dx[a]
                    yy = now[1] + dy[a]
                    if 0 <= xx < n and 0 <= yy < n and table[xx][yy] != 0 and board[xx][yy] == 0:
                        board[xx][yy] = cnt
                        temp += 1
                        q.append((xx, yy))
            res.append(temp)
print(cnt)
for i in sorted(res):
    print(i)