def closestNumbers(arr):
    arr.sort()

    # Find minimum difference
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        min_diff = min(min_diff, arr[i + 1] - arr[i])

    # Collect all pairs with minimum difference
    result = []
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == min_diff:
            result.extend([arr[i], arr[i + 1]])

    return result


# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(*closestNumbers(arr))