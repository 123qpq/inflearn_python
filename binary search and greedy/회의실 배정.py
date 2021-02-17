n = int(input())
meetings = []
for _ in range(n):
    meetings.append(tuple(map(int, input().split())))
meetings.sort(key = lambda x : (x[1], x[0]))

endtime = 0
cnt = 0
for start, end in meetings:
    if start >= endtime:
        endtime = end
        cnt += 1
print(cnt)