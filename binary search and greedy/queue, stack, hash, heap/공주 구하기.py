n, k = map(int, input().split())
princes = [i+1 for i in range(n)]
idx = k
for _ in range(n-1):
    princes.pop(idx-1)
    if idx == 0:
        idx += 1
    idx += k-1
    idx %= len(princes)
    
print(princes[0])