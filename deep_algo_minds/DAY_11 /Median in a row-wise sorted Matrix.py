from bisect import bisect_right

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])

        low, high = 1, 2000
        req = (n * m) // 2 + 1

        while low < high:
            mid = (low + high) // 2

            count = 0
            for row in mat:
                count += bisect_right(row, mid)

            if count < req:
                low = mid + 1
            else:
                high = mid

        return low
    
