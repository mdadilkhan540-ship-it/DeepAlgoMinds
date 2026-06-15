import sys

BITS = 61  # enough for numbers up to 1e18

def solve_query(L, R):
    lb = [(L >> i) & 1 for i in range(BITS - 1, -1, -1)]
    rb = [(R >> i) & 1 for i in range(BITS - 1, -1, -1)]

    # dp[pos][state]
    dp = [[0] * 4 for _ in range(BITS + 1)]

    for pos in range(BITS - 1, -1, -1):
        lbit = lb[pos]
        rbit = rb[pos]

        for state in range(4):
            tL = (state >> 1) & 1
            tR = state & 1

            low = lbit if tL else 0
            high = rbit if tR else 1

            best = 10**9

            for b in (0, 1):
                if b < low or b > high:
                    continue

                ntL = 1 if (tL and b == lbit) else 0
                ntR = 1 if (tR and b == rbit) else 0
                nstate = (ntL << 1) | ntR

                cost = b + dp[pos + 1][nstate]
                if cost < best:
                    best = cost

            dp[pos][state] = best

    # Reconstruct the smallest number having minimum popcount
    ans = 0
    state = 3  # tight to both L and R initially

    for pos in range(BITS):
        lbit = lb[pos]
        rbit = rb[pos]

        tL = (state >> 1) & 1
        tR = state & 1

        low = lbit if tL else 0
        high = rbit if tR else 1

        for b in (0, 1):  # choose smaller bit first -> smallest number
            if b < low or b > high:
                continue

            ntL = 1 if (tL and b == lbit) else 0
            ntR = 1 if (tR and b == rbit) else 0
            nstate = (ntL << 1) | ntR

            if b + dp[pos + 1][nstate] == dp[pos][state]:
                ans = (ans << 1) | b
                state = nstate
                break

    return ans


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1

    out = []
    for _ in range(t):
        L = data[idx]
        R = data[idx + 1]
        idx += 2
        out.append(str(solve_query(L, R)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
