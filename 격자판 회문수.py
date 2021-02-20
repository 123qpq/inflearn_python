table = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        if table[i][j] == table[i][j+4] and table[i][j+1] == table[i][j+3]:
            cnt += 1
        if table[j][i] == table[j+4][i] and table[j+1][i] == table[j+3][i]:
            cnt += 1
print(cnt)