import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1

ans = []

for _ in range(t):
    n = data[idx]
    idx += 1

    ones = 0
    for i in range(n):
        ones += data[idx + i] & 1
    idx += n

    zeros = n - ones

    if (ones % 2) + (zeros % 2) <= 1:
        ans.append("1")
    else:
        ans.append("0")

print("\n".join(ans))