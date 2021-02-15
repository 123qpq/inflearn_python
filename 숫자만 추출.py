import sys

word = sys.stdin.readline()
answer = ""
for i in word:
    if i.isdecimal():
        answer += i
answer = int(answer)
print(answer)
cnt = 0
for i in range(1, answer+1):
    if answer % i == 0:
        cnt += 1
print(cnt)