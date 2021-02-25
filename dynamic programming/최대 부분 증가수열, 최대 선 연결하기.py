n = int(input())
nums = [0] + list(map(int, input().split()))
cnt = [1] * (n+1)
for i in range(2, n+1): # i 가 전진
    maxi = 0
    for j in range(i-1, 0, -1): #j 가 탐색
        if nums[i] > nums[j] and cnt[j] > maxi:
            maxi = cnt[j]
    cnt[i] = maxi+1
print(max(cnt))