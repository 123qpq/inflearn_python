from collections import deque

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
q = deque()
cnt = 0
for i in range(n):
    for j in range(n):
        if table[i][j] == 1:
            table[i][j] = 0
            q.append((i, j))
            while q:
                now = q.popleft()
                for a in range(8):
                    xx = now[0] + dx[a]
                    yy = now[1] + dy[a]
                    if 0 <= xx < n and 0 <= yy < n and table[xx][yy] == 1:
                        table[xx][yy] = 0
                        q.append((xx, yy))
            cnt += 1
print(cnt)