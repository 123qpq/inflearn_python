import sys

n = int(sys.stdin.readline())

for i in range(n):
    word = input().lower()
    if word == word[::-1]:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")