from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        ans = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            ans = max(ans, (prefix_sum + i) // (i + 1))  # ceil(prefix_sum/(i+1))

        return ans
        
        
