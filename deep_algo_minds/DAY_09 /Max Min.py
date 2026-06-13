def maxMin(k, arr):
    arr.sort()

    min_unfairness = float('inf')

    for i in range(len(arr) - k + 1):
        min_unfairness = min(
            min_unfairness,
            arr[i + k - 1] - arr[i]
        )

    return min_unfairness

n = int(input())
k = int(input())

arr = [int(input()) for _ in range(n)]

print(maxMin(k, arr))
