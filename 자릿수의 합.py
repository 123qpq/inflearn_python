n = int(input())
nums = list(input().split())
maxsum = 0
for num in nums:
    newsum = sum(map(int, list(num)))
    if  newsum > maxsum:
        maxsum = newsum
        res = num
print(res)