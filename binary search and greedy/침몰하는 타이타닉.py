from collections import deque

n, maxweights = map(int, input().split())
weights = list(map(int, input().split()))
cnt = 0
weights.sort()
weights = deque(weights)
while weights:
    if len(weights) == 1:
        cnt += 1
        break
    if weights[0] + weights[-1] <= maxweights:
        weights.pop()
        weights.popleft()
    else:
        weights.pop()
    cnt += 1
print(cnt)