n = int(input())
boxes = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    minbox = boxes.index(min(boxes))
    maxbox = boxes.index(max(boxes))
    boxes[minbox] += 1
    boxes[maxbox] -= 1
print(max(boxes) - min(boxes))