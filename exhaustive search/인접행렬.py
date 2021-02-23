n, m = map(int, input().split())
table = [[0] * n for _ in range(n)]
for _ in range(m):
    x, y, len = map(int, input().split())
    table[x-1][y-1] = len

for i in range(n):
    for j in range(n):
        print(table[i][j], end=' ')
    print()
