
def minutes(runtime):
    temp = 0
    cnt = 1
    for dvd in dvdlist:
        if temp + dvd <= runtime:
            temp += dvd
        else:
            temp = dvd
            cnt += 1
    return cnt

n, m = map(int, input().split())
dvdlist = list(map(int, input().split()))
lt = max(dvdlist)
rt = sum(dvdlist)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if minutes(mid) > m:
        lt = mid + 1
    else:
        res = mid
        rt = mid -1
print(res)




