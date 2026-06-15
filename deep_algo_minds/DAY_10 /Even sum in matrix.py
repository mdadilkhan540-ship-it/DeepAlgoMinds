import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = [list(map(lambda x: int(x) & 1, input().split())) for _ in range(n)]

ans = 0

for top in range(n):
    col = [0] * m

    for bottom in range(top, n):
        for j in range(m):
            col[j] ^= a[bottom][j]

        parity = 0
        even_cnt = 1  # empty prefix
        odd_cnt = 0

        for x in col:
            parity ^= x

            if parity == 0:
                ans += even_cnt
                even_cnt += 1
            else:
                ans += odd_cnt
                odd_cnt += 1

print(ans)
