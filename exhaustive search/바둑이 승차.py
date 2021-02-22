from collections import deque

def dfs(l, sum, tsum):
    global res
    if sum + (total-tsum) < res:
        return
    if sum > c:
        return
    if l == n:
        if sum > res:
            res = sum
    else:
            dfs(l+1, sum+a[l], tsum+a[l])
            dfs(l+1, sum, tsum+a[l])

if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    total = sum(a)
    res = 0
    dfs(0, 0, 0)
    print(res)