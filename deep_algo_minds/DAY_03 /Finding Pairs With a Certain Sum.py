from collections import Counter
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]

        self.freq2[old] -= 1
        if self.freq2[old] == 0:
            del self.freq2[old]

        self.nums2[index] += val
        new = self.nums2[index]

        self.freq2[new] += 1

    def count(self, tot: int) -> int:
        ans = 0

        for x in self.nums1:
            ans += self.freq2.get(tot - x, 0)

        return ans
