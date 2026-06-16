class Solution:
    def maxArea(self, mat):
        if not mat:
            return 0

        n = len(mat)
        m = len(mat[0])

        heights = [0] * m
        ans = 0

        for i in range(n):
            # Update histogram heights
            for j in range(m):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            ans = max(ans, self.largestHistogram(heights))

        return ans

    def largestHistogram(self, heights):
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            curr = 0 if i == n else heights[i]

            while stack and heights[stack[-1]] > curr:
                h = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area
    
