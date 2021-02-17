import sys

n, m = map(int, input().split())
line = list(map(int, input().split()))
lt = 0
rt = 1
summ = line[0]
cnt = 0

while True:
    if summ < m:
        if rt < n:
            summ += line[rt]
            rt += 1
        else:
            break
    elif summ == m:
        cnt += 1
        summ -= line[lt]
        lt += 1
    else:
        summ -= line[lt]
        lt += 1
print(cnt)
