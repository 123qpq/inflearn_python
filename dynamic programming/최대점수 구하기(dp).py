n, m = map(int, input().split())
dy = [0] * (m+1)
for _ in range(n):
    ps, pt = map(int, input().split())
    for j in range(pt, m+1):
        dy[j] = max(dy[j], dy[j-pt] + ps)
print(dy[m])