from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid[0])

        for row in grid:
            left, right = 0, n - 1

            while left <= right:
                mid = (left + right) // 2

                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1

            ans += n - left

        return ans
    