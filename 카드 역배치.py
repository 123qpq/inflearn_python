import sys

cards = list(range(21))
for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        cards[a+i], cards[b-i] = cards[b-i], cards[a+i]
for i in cards[1:]:
    print(i, end=" ")
