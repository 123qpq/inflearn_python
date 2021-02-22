import sys
def dfs(l, sum):
    if l == n and sum==f:
            for x in res:
                print(x, end=" ")
            sys.exit(0)
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] =1
                res[l] = i
                dfs(l+1, sum+(mul[l]*res[l]))
                check[i]=0

if __name__ == "__main__":
    n, f = map(int, input().split())
    res = [0] * n
    mul = [1] * n
    check = [0] * (n+1)
    for i in range(1, n):
        mul[i] = mul[i-1]*(n-i)//i
    dfs(0, 0)