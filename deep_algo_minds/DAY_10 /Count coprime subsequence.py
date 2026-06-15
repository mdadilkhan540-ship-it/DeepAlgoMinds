import sys

MOD = 1000000007

# ---------- Read all testcases first ----------
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
ptr = 1

tests = []
maxA = 0

for _ in range(t):
    n = data[ptr]
    ptr += 1

    arr = data[ptr:ptr + n]
    ptr += n

    tests.append(arr)

    if arr:
        maxA = max(maxA, max(arr))

# ---------- Linear sieve for Mobius ----------
mu = [0] * (maxA + 1)
mu[1] = 1

primes = []
is_comp = [False] * (maxA + 1)

for i in range(2, maxA + 1):
    if not is_comp[i]:
        primes.append(i)
        mu[i] = -1

    for p in primes:
        v = i * p
        if v > maxA:
            break

        is_comp[v] = True

        if i % p == 0:
            mu[v] = 0
            break
        else:
            mu[v] = -mu[i]

# ---------- Divisors for every value ----------
divs = [[] for _ in range(maxA + 1)]

for d in range(1, maxA + 1):
    for multiple in range(d, maxA + 1, d):
        divs[multiple].append(d)

# ---------- Solve ----------
out = []

for arr in tests:
    S = [0] * (maxA + 1)

    ans = 0

    for x in arr:
        cop = 0

        for d in divs[x]:
            cop += mu[d] * S[d]

        dp = (1 + cop) % MOD

        ans += dp
        ans %= MOD

        for d in divs[x]:
            S[d] += dp
            if S[d] >= MOD:
                S[d] %= MOD

    out.append(str(ans))

sys.stdout.write("\n".join(out))
