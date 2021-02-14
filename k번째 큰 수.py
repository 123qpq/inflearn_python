import sys

n, k = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
res = []
for i in range(n):
    for j in range(i+1, n):
        for l in range(j+1, n):
            res.append(cards[i]+cards[j]+cards[l])
print(sorted(set(res), reverse=True)[k-1])
