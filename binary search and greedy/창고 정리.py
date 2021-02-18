n = int(input())
boxes = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    boxes.sort()
    boxes[0] += 1
    boxes[-1] -= 1
print(boxes[-1] - boxes[0])