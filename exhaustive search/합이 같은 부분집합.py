import sys

def dfs(level, sum):
    if sum > total // 2:
        return
    if level == n:
        if sum == total - sum: 
            print("YES")
            sys.exit(0)
    else:
        dfs(level+1, sum + num[level])
        dfs(level+1, sum)

if __name__ == "__main__":
    n = int(input())
    num = list(map(int, input().split()))
    total = sum(num)
    dfs(0, 0)
    print("NO")