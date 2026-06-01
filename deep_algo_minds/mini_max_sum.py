def miniMaxSum(arr):
    total = sum(arr)
    min_sum = total - max(arr)
    max_sum = total - min(arr)
    print(min_sum, max_sum)

arr = list(map(int, input().split()))
miniMaxSum(arr) 
