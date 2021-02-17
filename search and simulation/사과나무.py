n = int(input())

apples = [list(map(int, input().split())) for _ in range(n)]
res = sum(apples[n//2])
for i in range(n//2):
    res += sum(apples[i][n//2-i:n//2+1+i])
    res += sum(apples[n-i-1][n//2-i:n//2+1+i])
print(res)