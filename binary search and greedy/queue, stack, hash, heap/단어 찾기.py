n = int(input())
dic = []
for _ in range(n):
    dic.append(input())

for _ in range(n-1):
    dic.pop(dic.index(input()))
print(dic[0])

