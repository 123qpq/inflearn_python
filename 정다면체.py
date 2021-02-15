import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}

for i in range(1, n+1):
    for j in range(1, m+1):
        dic[i+j] = dic.get(i+j, 0) + 1
answer = ""
for x in dic:
    if dic[x] == max(dic.values()):
        answer += f"{x} "

print(answer[:-1])
