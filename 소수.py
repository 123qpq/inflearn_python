n = int(input())
cnt = 0
lst = [True] * (n+1)
for i in range(2, n+1):
    if lst[i]:
        cnt += 1
        for j in range(2 * i, n+1, i):
            lst[j] = False
print(cnt)
