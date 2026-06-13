def superDigit(n, k):
    initial_sum = sum(int(d) for d in n) * k

    def digit_sum(x):
        if x < 10:
            return x
        return digit_sum(sum(int(d) for d in str(x)))

    return digit_sum(initial_sum)

n, k = input().split()
print(superDigit(n, int(k)))
