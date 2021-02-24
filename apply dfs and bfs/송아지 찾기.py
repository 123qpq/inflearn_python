start, end = map(int, input().split())
length = end - start
if length < 0:
    print(length)
else:
    res = 0
    res += length // 5
    rest = length % 5
    if rest == 0:
        pass
    elif rest < 4:
        res += rest
    elif rest == 4:
        res += 2
    print(res)