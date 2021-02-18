res = 0

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for _ in range(m):
    row, direc, rot = map(int, input().split())
    rot %= n
    if direc: #오른쪽
        table[row-1] = table[row-1][n - rot:] + table[row-1][:n - rot]
    else: #왼쪽
        table[row-1] = table[row-1][rot:] + table[row-1][:rot]
    #print(table)

for i in range(n//2):
    res += sum(table[i][i:n-i])
    res += sum(table[n-i-1][i:n-i])
res += table[n//2][n//2]
print(res)