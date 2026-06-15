def prefix_xor(n):
    if n < 0:
        return 0

    r = n % 8

    if r == 0 or r == 1:
        return n
    elif r == 2 or r == 3:
        return 2
    elif r == 4 or r == 5:
        return n + 2
    else:
        return 0


def xorSequence(l, r):
    return prefix_xor(r) ^ prefix_xor(l - 1)


q = int(input())

for _ in range(q):
    l, r = map(int, input().split())
    print(xorSequence(l, r))
    
    
