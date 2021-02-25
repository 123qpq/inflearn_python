n = int(input())
res = [1, 2]
for i in range(2, n): #'돌다리 건너기'일 경우 range(2, n+1)
    res.append(res[i-1] + res[i-2])
print(res[-1])
