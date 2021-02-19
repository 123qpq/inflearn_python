res = ''
n = int(input())
lst = list(map(int, input().split()))
lt = 0
rt = n-1
last = 0
temp = []
while lt <= rt:
    if last < lst[lt]:
        temp.append((lst[lt], 'L'))
    if last < lst[rt]:
        temp.append((lst[rt], 'R'))
    temp.sort()
    if len(temp) == 0:
        break
    else:
        res += temp[0][1]
        last = temp[0][0]
        if temp[0][1]=='L':
            lt += 1
        else:
            rt -= 1
    temp.clear()
print(len(res))
print(res)