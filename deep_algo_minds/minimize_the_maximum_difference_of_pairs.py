from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def can_make_pairs(max_diff):
            pairs = 0
            i = 1

            while i < len(nums):
                if nums[i] - nums[i - 1] <= max_diff:
                    pairs += 1
                    i += 2  # use both indices
                else:
                    i += 1

            return pairs >= p

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            if can_make_pairs(mid):
                right = mid
            else:
                left = mid + 1

        return left