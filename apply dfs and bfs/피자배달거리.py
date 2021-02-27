def dfs(l, s):
    global res
    if l == m:
        sum = 0
        for j in range(len(house)):
            x1 = house[j][0]
            y1 = house[j][1]
            dis = float('inf')
            for k in combi:
                x2 = pizza[k][0]
                y2 = pizza[k][1]
                dis = min(dis, abs(x1-x2) + abs(y1-y2))
            sum += dis
        if sum < res:
            res = sum
    else:
        for i in range(s, len(pizza)):
            combi[l] = i
            dfs(l+1, i+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    house = []
    pizza = []
    combi = [0] * m
    res = float('inf')
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                house.append((i, j))
            if table[i][j] == 2:
                pizza.append((i, j))
    dfs(0, 0)
    print(res)
