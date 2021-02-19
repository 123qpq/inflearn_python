n = int(input())
lst = list(map(int, input().split()))

for i in range(1, n):
    if lst[i] == 1 and lst[i-1] != 0:
        lst[i] = lst[i-1] + 1
print(sum(lst))
