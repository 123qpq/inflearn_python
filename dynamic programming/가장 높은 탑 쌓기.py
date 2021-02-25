n = int(input())
brick = [ tuple(map(int, input().split())) for i in range(n)]
brick.sort(reverse = True)
print(brick)
cnt = [0] * n
cnt[0] = brick[0][1]
for i in range(1, n): # i 가 전진
    maxh = 0
    for j in range(i): #j 가 탐색
        if brick[j][2] > brick[i][2] and cnt[j] > maxh:
            maxh = cnt[j]
    cnt[i] = maxh + brick[i][1]
print(max(cnt))