from collections import defaultdict
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = defaultdict(int)

    for i, x in enumerate(a, start=1):  # 1-based index
        freq[x ^ i] += 1

    ans = 0
    for f in freq.values():
        ans += f * (f - 1) // 2

    print(ans)