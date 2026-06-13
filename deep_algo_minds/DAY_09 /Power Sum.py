def powerSum(X, N, num=1):
    power = num ** N

    if power == X:
        return 1

    if power > X:
        return 0

    return powerSum(X - power, N, num + 1) + powerSum(X, N, num + 1)

X = int(input())
N = int(input())

print(powerSum(X, N))
