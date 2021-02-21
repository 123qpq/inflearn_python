n = int(input())
dic = {}
for _ in range(n):
    dic[input()] = 0

for _ in range(n-1):
    dic[input()] += 1

for key, value in dic.items():
    if value == 0:
        print(key)