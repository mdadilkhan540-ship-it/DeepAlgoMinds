class Solution:
    def summaryRanges(self, nums):
        res = []

        for i, num in enumerate(nums):
            # Start of a new range
            if i == 0 or nums[i - 1] + 1 != num:
                start = num

            # End of the current range
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                if start == num:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{num}")

        return res