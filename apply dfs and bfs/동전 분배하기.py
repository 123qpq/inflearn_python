def dfs(l):
    global res
    if l == n:
        if len(set(people)) == 3:
            res = min(res, (max(people)-min(people)))
    else:
        for i in range(3):
            people[i] += coins[l]
            dfs(l+1)
            people[i] -= coins[l]


if __name__ == "__main__":
    n = int(input())
    coins = []
    people = [0, 0, 0]
    res = float('inf')
    for _ in range(n):
        coins.append(int(input()))
    dfs(0)
    print(res)
