n = int(input())
lst = list(map(int, input().split()))
reverse = []
for idx, x in enumerate(reversed(lst)):
    reverse.insert(x, n-idx)
for i in reverse:
    print(i, end = ' ')