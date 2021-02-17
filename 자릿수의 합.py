n = int(input())
nums = list(input().split())
sums = []
for num in nums:
    sums.append(sum(map(int, list(num))))
print(nums[sums.index(max(sums))])