def hamming_weight(n):
    return bin(n).count('1')

n = int(input())
arr = list(map(int, input().split()))

arr.sort(key=lambda x: (hamming_weight(x), x))

print(*arr)
