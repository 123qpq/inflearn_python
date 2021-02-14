import sys

tc = int(sys.stdin.readline())
for i in range(tc):
    n, s, e, k = map(int, sys.stdin.readline().split())
    test = list(map(int, sys.stdin.readline().split()))[s-1:e]
    print(f"#{i+1} {sorted(test)[k-1]}")