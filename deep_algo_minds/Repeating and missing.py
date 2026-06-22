class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        freq = [0] * (n + 1)

        for num in arr:
            freq[num] += 1

        duplicate = missing = 0

        for i in range(1, n + 1):
            if freq[i] == 2:
                duplicate = i
            elif freq[i] == 0:
                missing = i

        return [duplicate, missing]
    