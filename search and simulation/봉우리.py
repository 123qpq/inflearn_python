n = int(input())
table = [[0 for _ in range(n+2)]]
for i in range(n):
    table.append([0] + list(map(int, input().split())) + [0])
table.append([0 for _ in range(n+2)])

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if max(table[i-1][j], table[i+1][j], table[i][j+1], table[i][j-1]) < table[i][j]:
            cnt += 1
print(cnt)
