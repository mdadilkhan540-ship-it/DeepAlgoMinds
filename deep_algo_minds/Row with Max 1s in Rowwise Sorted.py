class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])

        max_ones = 0
        ans = -1

        for i in range(n):
            low, high = 0, m - 1
            first_one = m

            while low <= high:
                mid = (low + high) // 2

                if arr[i][mid] == 1:
                    first_one = mid
                    high = mid - 1
                else:
                    low = mid + 1

            ones = m - first_one

            if ones > max_ones:
                max_ones = ones
                ans = i

        return ans
    