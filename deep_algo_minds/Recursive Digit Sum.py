
import os

def superDigit(n, k):
    total = sum(int(d) for d in n) * k

    while total >= 10:
        total = sum(int(d) for d in str(total))

    return total

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]
    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)
    
