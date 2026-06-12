from bisect import bisect_left
from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0

        for x in arr1:
            i = bisect_left(arr2, x)

            valid = True

            if i < len(arr2) and abs(arr2[i] - x) <= d:
                valid = False

            if i > 0 and abs(arr2[i - 1] - x) <= d:
                valid = False

            if valid:
                ans += 1

        return ans
    
    
