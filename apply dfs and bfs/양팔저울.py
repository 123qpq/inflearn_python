def dfs(l, sum):
    global res
    if l == n:
        if 0 < sum:
            res.add(sum)
    else:
        dfs(l+1, sum + chu[l])
        dfs(l+1, sum - chu[l])
        dfs(l+1, sum)


if __name__ == "__main__":
    n = int(input())
    chu = list(map(int, input().split()))
    chusum = sum(chu)
    res = set()
    dfs(0, 0)
    print(chusum - len(res))