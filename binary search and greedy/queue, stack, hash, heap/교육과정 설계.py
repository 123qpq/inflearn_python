edu = input()
n = int(input())
plans = [input() for _ in range(n)]
for plan in plans:
    idx = 0
    for p in plan:
        if p in edu:
            if p == edu[idx]:
                idx += 1
            else:
                print("NO")
                break
    else:
        print("YES")