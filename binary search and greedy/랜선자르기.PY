import sys

def count(len):
    cnt = 0
    for line in lines:
        cnt += line // len
    return cnt

n, k  = map(int, input().split())
lines = []
res = 0
for _ in range(n):
    lines.append(int(input()))
lt = 1
rt = max(lines)

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= k:
        res = mid

        lt = mid + 1
    else:
        rt = mid - 1
print(res)