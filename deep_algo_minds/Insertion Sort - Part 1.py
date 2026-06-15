def insertionSort1(n, arr):
    value = arr[n - 1]
    i = n - 2

    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1

    arr[i + 1] = value
    print(*arr)

n = int(input())
arr = list(map(int, input().split()))

insertionSort1(n, arr)
