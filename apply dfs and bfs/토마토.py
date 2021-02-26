import sys
from collections import deque
m, n = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
q = deque()
res = 0

for i in range(n):
    for j in range(m):
        if table[i][j] == 1:
            q.append((i, j))
while q:
    temp = q.popleft()
    for i in range(4):
        xx = temp[0] + dx[i]
        yy = temp[1] + dy[i]
        if 0 <= xx < n and 0 <= yy < m and table[xx][yy] == 0:
            table[xx][yy] = table[temp[0]][temp[1]] + 1
            q.append((xx, yy))

for i in range(n):
    for j in range(m):
        if table[i][j] == 0:
            print(-1)
            sys.exit(0)
        res = max(res, table[i][j])
print(res-1)
