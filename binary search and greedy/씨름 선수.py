n = int(input())
body = []
for i in range(n):
    body.append(tuple(map(int, input().split())))

body.sort(reverse = True)
largest = 0
cnt = 0
for height, weight in body:
    if weight > largest:
        largest = weight
        cnt += 1
print(cnt)