n, m = map(int, input().split())
table = [[float('inf')]*n for _ in range(n)]
for _ in range(m):
    x, y, cost = map(int, input().split())
    table[x-1][y-1] = cost
for k in range(n):
    for i in range(n):
        table[i][i] = 0
        for j in range(n):
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])
for i in range(n):
    for j in range(n):
        if table[i][j] == float('inf'):
            table[i][j] = 'M'
    print(' '.join(str(x) for x in table[i]))