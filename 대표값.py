import sys

n = int(sys.stdin.readline())
grades = list(map(int, sys.stdin.readline().split()))
ave = int((sum(grades) / n) + 0.5)
diff = float('inf')

for i, grade in enumerate(grades):
    tdiff = abs(ave - grade)
    if tdiff < diff:
        diff = tdiff
        idx = i
    elif tdiff == diff:
        idx = grades.index(max(grades[idx], grades[i]))

print(ave, idx+1)