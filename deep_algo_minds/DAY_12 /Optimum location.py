from math import sqrt

class Solution:
    
    def totalDistance(self, x, points, a, b, c):
        y = (-c - a * x) / b
        dist = 0

        for px, py in points:
            dist += sqrt((x - px) ** 2 + (y - py) ** 2)

        return dist

    def findOptimumCost(self, points, line):
        a, b, c = line

        low = -10000
        high = 10000

        for _ in range(100):
            mid1 = low + (high - low) / 3
            mid2 = high - (high - low) / 3

            d1 = self.totalDistance(mid1, points, a, b, c)
            d2 = self.totalDistance(mid2, points, a, b, c)

            if d1 < d2:
                high = mid2
            else:
                low = mid1

        return self.totalDistance((low + high) / 2, points, a, b, c)
    
