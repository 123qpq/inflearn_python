def reverse(num):
    return int(num[::-1])

def isPrime(num):
    if num == 1:
        return
    for i in range(2, num):
        if num % i == 0:
            return
    return num

n = int(input())
lst = input().split()

for i in lst:
    n = isPrime(reverse(i))
    if n is not None:
        print(n, end = " ")