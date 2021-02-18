n, maxweights = map(int, input().split())
weights = list(map(int, input().split()))
cnt = 0
weights.sort()
while weights:
    if weights[0] + weights[-1] <= maxweights:
        weights.pop()
        weights.pop(0)
    else:
        weights.pop()
    cnt += 1
print(cnt)