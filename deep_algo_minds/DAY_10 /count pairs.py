import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    even = 0
    for x in arr:
        if x % 2 == 0:
            even += 1

    odd = n - even
    print(even * odd)
    
