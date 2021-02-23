def dfs(len):
    if memo[len] > 0:
        return memo[len]
    if len == 1 or len == 2:
        return len
    else:
        memo[len] = dfs(len-1) + dfs(len-2)
        return memo[len]

if __name__ == "__main__":
    n = int(input())
    memo = [0] * (n+1)
    print(dfs(n))