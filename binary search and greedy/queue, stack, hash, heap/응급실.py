from collections import deque

n, m = map(int, input().split())
patients = list(map(int, input().split()))
patients = [(i, p) for i, p in enumerate(patients)]
patients = deque(patients)
cnt = 0

while True:
    cur = patients.popleft()
    if any(cur[1] < x[1] for x in patients):
        patients.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break