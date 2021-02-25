from collections import deque
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
sum = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
check[n//2][n//2] = 1
sum += table[n//2][n//2]
q.append((n//2, n//2))
l = 0
while True:
    if l == n//2:
        break
    size = len(q)
    for i in range(size):
        temp = q.popleft()
        for j in range(4):
            x = temp[0] + dx[j]
            y = temp[1] + dy[j]
            if check[x][y] == 0:
                sum += table[x][y]
                check[x][y] = 1
                q.append((x, y))
    l += 1
    print(l, size)
    for x in check:
        print(x)
print(sum)