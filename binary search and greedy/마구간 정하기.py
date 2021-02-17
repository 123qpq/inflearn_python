def pointer(length):
    put = stables[0]
    cnt = 1
    for stable in stables:
        if stable - put >= length:
            put = stable
            cnt += 1
    return cnt

n, horses = map(int, input().split())
stables = []
for i in range(n):
    stables.append(int(input()))
    
stables.sort()
lt = stables[0]
rt = stables[-1]

while lt <= rt:
    mid = (lt + rt) // 2
    if pointer(mid) < horses:
        rt = mid -1
    else:
        res = mid
        lt = mid + 1
print(res)
