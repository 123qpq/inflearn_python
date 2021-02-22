num, n = input().split()
temp = []
n = int(n)
num = list(map(int, num))
while num:
    if temp and temp[-1] < num[0] and n != 0:
        temp.pop()
        n -= 1
    else:
        temp.append(num.pop(0))
if n != 0:
    temp = temp[:-n]

print(''.join(map(str, temp)))