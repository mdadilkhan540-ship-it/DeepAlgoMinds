t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    operations = 0

    for i in range(n):
        while arr[i] % 2 == 0:
            arr[i] //= 2
            operations += 1

    print(operations)
    