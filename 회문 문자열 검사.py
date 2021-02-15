import sys

n = int(sys.stdin.readline())

for i in range(n):
    word = input().lower()
    wlen = len(word) // 2
    if word[:wlen] == word[:len(word)-wlen-1:-1]:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")