class Solution:
    def findPair(self, arr, x):
        arr.sort()
        n = len(arr)

        i = 0
        j = 1

        while j < n:
            diff = arr[j] - arr[i]

            if i != j and diff == x:
                return True
            elif diff < x:
                j += 1
            else:
                i += 1

            if i == j:
                j += 1

        return False
    
