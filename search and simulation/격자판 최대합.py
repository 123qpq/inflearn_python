n = int(input())

table = [list(map(int, input().split())) for _ in range(n)]
res = 0

leftcross = 0
rightcross = 0
for i in range(n):
    leftcross += table[i][i]
    rightcross += table[n-i-1][i]
    temp1 = temp2 = 0
    for j in range(n):
        temp1 += table[j][i]
        temp2 += table[i][j]
    res = max(res, temp1, temp2)
print(max(res, leftcross, rightcross))
