n = int(input())
table = [[float('inf')]* n for _ in range(n)]
while True:
    s, e = map(int, input().split())
    if s == -1 and e == -1:
        break
    table[s-1][e-1] = 1
    table[e-1][s-1] = 1

for k in range(n):
    for i in range(n):
        table[i][i] = 0
        for j in range(n):
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])

score = float('inf')
candidate = []
for t in table:
    score = min(score, max(t))
for i in range(n):
    if max(table[i]) == score:
        candidate.append(str(i+1))
print(table)
print(score, len(candidate))
for x in candidate:
    print(x, end = ' ')